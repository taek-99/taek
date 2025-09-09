from django.db import transaction, models
from django.utils import timezone
from datetime import timedelta
from .models import Inventory, Order, HOLD_MINUTES

@transaction.atomic
def place_hold(event_id: int, inventory_ids: list[int], customer_id: str) -> str:
    """
    좌석/인벤토리 배열을 5분 동안 임시 홀드.
    select_for_update(skip_locked=True)로 동시성 잠금.
    """
    now = timezone.now()
    qs = (Inventory.objects
          .select_for_update(skip_locked=True)
          .filter(event_id=event_id, id__in=inventory_ids, is_sold=False)
          .filter(models.Q(hold_until__lt=now) | models.Q(hold_until__isnull=True)))
    rows = list(qs)
    if len(rows) != len(inventory_ids):
        raise ValueError("Some seats are not available")

    hold_token = f"{customer_id}-{now.timestamp()}"
    until = now + timedelta(minutes=HOLD_MINUTES)

    for r in rows:
        r.hold_until = until
        r.hold_token = hold_token
    Inventory.objects.bulk_update(rows, ['hold_until', 'hold_token'])
    return hold_token

@transaction.atomic
def confirm_purchase(hold_token: str, idempotency_key: str) -> Order:
    """
    홀드된 인벤토리를 판매 확정(is_sold=True)하고 주문 생성.
    멱등성 키로 중복 결제 방지.
    """
    # 이미 같은 키로 생성된 주문이 있으면 그대로 반환
    existing = Order.objects.filter(idempotency_key=idempotency_key).first()
    if existing:
        return existing

    now = timezone.now()
    rows = list(Inventory.objects.select_for_update()
                .filter(hold_token=hold_token, is_sold=False, hold_until__gt=now))
    if not rows:
        raise ValueError("Hold expired or already sold")

    total = sum(r.ticket_type.price for r in rows)
    evt = rows[0].event

    for r in rows:
        r.is_sold = True
        r.hold_until = None
        r.hold_token = ""
    Inventory.objects.bulk_update(rows, ['is_sold', 'hold_until', 'hold_token'])

    order = Order.objects.create(
        event=evt,
        hold_token=hold_token,
        idempotency_key=idempotency_key,
        total_amount=total,
    )
    return order

def release_expired_holds():
    """ 만료된 홀드 해제(크론/커맨드/관리자액션에서 호출) """
    now = timezone.now()
    stale = (Inventory.objects
             .filter(hold_until__isnull=False, hold_until__lte=now, is_sold=False))
    for r in stale:
        r.hold_until = None
        r.hold_token = ""
    Inventory.objects.bulk_update(stale, ['hold_until', 'hold_token'])
    return stale.count()

import uuid
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_POST
from .models import Event, Inventory
from .services import place_hold, confirm_purchase

def index(request):
    events = Event.objects.select_related('venue').order_by('starts_at')
    return render(request, 'events/index.html', {'events': events})

def detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'events/detail.html', {'event': event})

def availability(request, pk):
    """이벤트 좌석 상태 JSON (단순화)"""
    event = get_object_or_404(Event, pk=pk)
    inv = (Inventory.objects
           .select_related('seat','ticket_type')
           .filter(event=event)
           .values('id','seat__section','seat__row','seat__number','is_sold','hold_until'))
    return JsonResponse({'event': event.id, 'inventory': list(inv)})

@require_POST
def hold(request, pk):
    """선택한 인벤토리 ID들을 홀드"""
    event = get_object_or_404(Event, pk=pk)
    ids = request.POST.getlist('inventory_ids[]') or request.POST.getlist('inventory_ids')
    try:
        ids = [int(x) for x in ids]
        hold_token = place_hold(event.id, ids, customer_id=str(request.user or 'anon'))
    except Exception as e:
        return HttpResponseBadRequest(str(e))
    # 임시로 세션에 보관(데모용)
    request.session['hold_token'] = hold_token
    return redirect('events:detail', pk=event.pk)

@require_POST
def checkout_confirm(request):
    """홀드 토큰으로 결제확정 (데모: 결제 과정 생략)"""
    hold_token = request.POST.get('hold_token') or request.session.get('hold_token')
    if not hold_token:
        return HttpResponseBadRequest("No hold token")
    idem = request.POST.get('idempotency_key') or uuid.uuid4().hex
    try:
        order = confirm_purchase(hold_token, idem)
    except Exception as e:
        return HttpResponseBadRequest(str(e))
    # 성공 페이지(간단히)
    return render(request, 'events/success.html', {'order': order})

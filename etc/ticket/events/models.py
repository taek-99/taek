from django.db import models
from django.utils import timezone
from datetime import timedelta

HOLD_MINUTES = 5

class Venue(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200, blank=True)
    def __str__(self): return self.name

class Event(models.Model):
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    starts_at = models.DateTimeField()
    poster = models.ImageField(upload_to='events/%Y/%m/%d/', blank=True)
    on_sale = models.BooleanField(default=True)
    capacity = models.PositiveIntegerField(default=0)
    def __str__(self): return f'{self.title} @ {self.venue}'

# 좌석(고정 좌석제 예시)
class Seat(models.Model):
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    section = models.CharField(max_length=50)
    row = models.CharField(max_length=10)
    number = models.CharField(max_length=10)
    class Meta:
        unique_together = ('venue', 'section', 'row', 'number')
    def __str__(self): return f'{self.section}-{self.row}-{self.number}'

# 가격/등급
class TicketType(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)  # R/S/A 등
    price = models.PositiveIntegerField()
    def __str__(self): return f'{self.event} - {self.name}'

# 이벤트별 좌석 인벤토리 (한 좌석당 1개)
class Inventory(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.PROTECT)
    ticket_type = models.ForeignKey(TicketType, on_delete=models.PROTECT)
    is_sold = models.BooleanField(default=False)
    hold_until = models.DateTimeField(null=True, blank=True)
    hold_token = models.CharField(max_length=100, blank=True, default="")
    class Meta:
        unique_together = ('event', 'seat')
        indexes = [
            models.Index(fields=['event', 'is_sold']),
            models.Index(fields=['hold_until']),
        ]
    @property
    def is_held(self):
        return self.hold_until and self.hold_until > timezone.now()

# 주문(아주 간단히)
class Order(models.Model):
    event = models.ForeignKey(Event, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    hold_token = models.CharField(max_length=100)     # 어떤 홀드로 결제했는지
    idempotency_key = models.CharField(max_length=100, unique=True)  # 중복 결제 방지
    total_amount = models.PositiveIntegerField(default=0)

from django.db import models
from core import models as core_model
from django.utils import timezone

class Reservation(core_model.TimeStampedModel):

    """Reservation Model Definition"""

    STATUS_PENDING = 'pending'
    STATUS_CONFIRM = 'confirm'
    STATUS_CANCELED = 'canceled'

    STATUS_CHOICES = (
        (STATUS_PENDING, 'Pending'),
        (STATUS_CONFIRM, 'Confirm'),
        (STATUS_CANCELED, 'Canceled'),
    )

    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default=STATUS_PENDING)
    guest = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='reservations')
    room = models.ForeignKey('rooms.Room', on_delete=models.CASCADE, related_name='reservations')
    check_in = models.DateField()
    check_out = models.DateField()

    def __str__(self):
        return f'{self.room} - {self.check_in}'

    def in_progress(self):
        today = timezone.now().date()
        return self.check_in <= today and self.check_out >= today

    in_progress.boolean = True

    def is_finished(self):
        today = timezone.now().date()
        return today > self.check_out

    is_finished.boolean = True
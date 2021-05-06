from django.db import models
from base.models import Firm, Subsidiary, Project
from base.models import CATEGORY_CHOICES

CURRENCY_CHOICES = [
    ('TRY', 'TRY'),
    ('USD', 'USD'),
    ('EUR', 'EUR'),
    ('GBP', 'GBP'),
    ('KWD', 'KWD'),
    ('UAH', 'UAH'),
    ('RUB', 'RUB'),
    ('SAR', 'SAR'),
    ('MKD', 'MKD'),
]

# Create your models here.
class Tender(models.Model):
    title = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    category = models.SmallIntegerField(choices=CATEGORY_CHOICES)
    #budget

class Offer(models.Model):
    tender = models.ForeignKey(Tender, on_delete=models.CASCADE)
    firm = models.ForeignKey(Firm, on_delete=models.CASCADE)
    offer_price = models.FloatField()
    currency = models.CharField(max_length=3,choices=CURRENCY_CHOICES)
    winner = models.BooleanField(default=False)
    # created_at  = models.DateTimeField(default = timezone.now,blank=True, null=True, editable = False)
    # modified_at = AutoDateTimeField(default = timezone.now, editable = False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['tender', 'winner'], name='unique_tender_winner'),
        ]
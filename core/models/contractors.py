from django import dispatch
from django.db import models
from django.db.models.signals import post_save

from base import Staff


class Contractor(Staff):
    balance = models.DecimalField(max_digits=12, decimal_places=2,
                                  blank=True, default=0.0)
    mileage = models.DecimalField(max_digits=12, decimal_places=2,
                                  blank=True, default=0.0)
    fund_balance = models.DecimalField(max_digits=12, decimal_places=2,
                                       blank=True, default=0.0)
    tag = models.CharField(
        max_length=15, default='shopperdriver',
        choices=(('shopperdriver', 'Shopper + Driver'),
                 ('shopper', 'Shopper'),
                 ('driver', 'Driver'),
                 ))

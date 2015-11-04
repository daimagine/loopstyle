from django.contrib.auth.models import User
from django.db import models
from rest_framework.authtoken.models import Token

from base import LoopstyleBase
from core import utils


class Customer(LoopstyleBase):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User)
    mobile_num = models.CharField(max_length=20, blank=False)
    image = models.ImageField(upload_to=utils.customer_upload_to,
                              max_length=200, blank=True, default='')
    status = models.CharField(
        max_length=25, default='pending',
        choices=(('pending', 'Pending'),
                 ('verified', 'Verified'),
                 ('deactivated', 'Deactivated'),
                 ('banned', 'Banned')))
    verified_email = models.BooleanField(default=False)
    verified_mobile = models.BooleanField(default=False)
    last_order_at = models.DateTimeField(blank=True, default=None, null=True)
    order_count = models.IntegerField(blank=False, default=0)

    @property
    def name(self):
        full_name = ' '.join([self.user.first_name, self.user.last_name])
        return '{} ({})'.format(self.user.username, full_name)

    def api_token(self):
        return Token.objects.get_or_create(user=self.user)

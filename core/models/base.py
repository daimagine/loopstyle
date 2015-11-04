from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields.files import ImageFieldFile
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from rest_framework.authtoken.models import Token

from core import utils


class LoopstyleBase(models.Model):
    def __unicode__(self):
        return u'[{}] {}'.format(self.id, self.name)

    @property
    def hashed_id(self):
        return utils.hasher_encode(self.id) if self.id else ''

    class Meta:
        abstract = True


class Staff(LoopstyleBase):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User)
    mobile_num = models.CharField(max_length=20, blank=False)
    image = models.ImageField(upload_to=utils.staff_upload_to,
                              max_length=200, blank=True, default='')
    rating = models.DecimalField(max_digits=3, decimal_places=1,
                                 blank=True, default=0.0)
    account_name = models.CharField(max_length=100)
    account_num = models.CharField(max_length=50)
    account_bank = models.CharField(
        max_length=10, default='bca',
        choices=(('bca', 'BCA'),
                 ('bni', 'BNI'),
                 ('bri', 'BRI'),
                 ('mandiri', 'Mandiri'),
                 ('cimb', 'CIMB')))

    @property
    def name(self):
        full_name = ' '.join([self.user.first_name, self.user.last_name])
        return '{} ({})'.format(self.user.username, full_name)

    def api_token(self):
        return Token.objects.get_or_create(user=self.user)

    @property
    def profile_image(self):
        return self.image_urls_dict(self.image, image_type='staff')

    class Meta:
        abstract = True


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

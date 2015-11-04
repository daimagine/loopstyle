from decimal import Decimal
import datetime
import math
import os
import uuid

from django.utils import timezone
from hashids import Hashids


_hasher = None


def hasher():
    global _hasher

    if not _hasher:
        _hasher = Hashids(salt='i am using this hash', min_length=12)

    return _hasher


def hasher_encode(plain_id):
    return hasher().encode(plain_id)


def hasher_decode(hash_id):
    return hasher().decode(hash_id)


def hasher_smart_decode(hash_id):
    original_id = hasher_decode(hash_id)
    if original_id:
        return int(original_id[0])


def json_default(obj):
    '''Default JSON serializer.'''
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()


def round_up(num, up_to):
    return int(math.ceil(num / Decimal(up_to))) * Decimal(up_to).quantize(
        Decimal('0.01'))


def to_jkt_isoformat(dt):
    jkt = timezone.get_fixed_timezone(420)
    return timezone.localtime(dt, jkt).isoformat()


def upload_to(prefix, instance, filename):
    unique_id = uuid.uuid4().hex
    _, sep, ext = filename.rpartition('.')
    uuid_filename = '{}.{}'.format(unique_id, ext)
    # Do we need to enforce any rule on the ext? lower case? must be jpg/png?
    return os.path.join('raw', prefix, uuid_filename)


def customer_upload_to(instance, filename):
    return upload_to('customer', instance, filename)


def staff_upload_to(instance, filename):
    return upload_to('staff', instance, filename)

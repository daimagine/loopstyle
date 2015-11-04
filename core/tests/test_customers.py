from django.core.urlresolvers import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from rest_framework.test import APITestCase

from core.models import Customer


class CustomerTestCase(TestCase):
    fixtures = ['fixtures/development/auth.User.json',
                'fixtures/development/core.Customer.json', ]

    def test_get_customer(self):
        customer = Customer.objects.get(pk=1)
        self.assertEqual(customer.mobile_num, '123456765')
        self.assertTrue(customer.verified_email)

    def test_get_customer_profile(self):
        # Include an appropriate `Authorization:` header on all requests.
        token = Token.objects.get(user__id=2)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        url = reverse('customer-profile-get')
        response = client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('first_name'), u'Customer')
        self.assertEqual(response.data.get('id'), u'gybv4xNArBoY')

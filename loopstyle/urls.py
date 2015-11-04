from __future__ import absolute_import

from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from rest_framework.authtoken import views as authtoken_views

from core import views as core_views


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')),  # grappelli URLS

    url(r'^products/$',
        core_views.ProductsRetrieve.as_view(),
        name='product-list-get'),

    url(r'^secure/customer/profile/$',
        core_views.CustomerProfileRetrieve.as_view(),
        name='customer-profile-get'),
    
    url(r'^secure/contractor/profile/$',
        core_views.ContractorProfileRetrieve.as_view(),
        name='contractor-profile-get'),
    
    url(r'^$', core_views.api_root),

    url(r'^secure/api-token-auth/', authtoken_views.obtain_auth_token),
    url(r'^api-token-auth/', authtoken_views.obtain_auth_token),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework'))
]

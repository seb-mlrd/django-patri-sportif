# www/urls.py
from django.urls import path
from .views import SportSiteList

urlpatterns = [
    path('', SportSiteList.as_view(), name='sport_site_list'),
]
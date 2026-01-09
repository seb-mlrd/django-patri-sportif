# www/urls.py
from django.urls import path
from .views import SportSiteList, SportSiteDetail

urlpatterns = [
    path('', SportSiteList.as_view(), name='sport_site_list'),
    path('site/<int:pk>/', SportSiteDetail.as_view(), name='sport_site_detail'),
]
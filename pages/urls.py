from django.urls import path, include
from pages.views import *


urlpatterns = [
    path('helo/', help),
    path("",homePageView, name='home'),
    path('1/', HomePageView.as_view(), name='homme'),
    path('1/', AboutPageView.as_view(), name='about')
]

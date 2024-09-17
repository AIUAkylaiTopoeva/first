from django.urls import path
from pages.views import *


urlpatterns = [
    path('helo/', help),
    path("",homePageView, name='homme'),
    path('home/', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about')
]

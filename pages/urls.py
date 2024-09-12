from django.urls import path, include
from pages.views import *

urlpatterns = [
    path('helo/', help),
    path("",homePageView, name='home')
]

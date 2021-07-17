from django.urls import path
from .views import *

urlpatterns = [
    path('profile', profile_list),
    path('profile/<pk>', profile_detail),
]

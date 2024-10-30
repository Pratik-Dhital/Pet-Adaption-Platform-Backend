from django.urls import path, include
from .views import *

urlpatterns = [
    path("contacts", ContactViewSet.as_view(), name='contacts')
    # path("contacts", ContactViewSet.as_view(), name='contacts')
    # path("contacts", ContactViewSet.as_view(), name='contacts')
]
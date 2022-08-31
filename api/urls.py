from django.urls import path

from .views import *

urlpatterns = [
    path('', Example_API.as_view(), name='example'),
]
from django.urls import path
from .views import Clip_Video_API

urlpatterns = [
    path("clip_video/", Clip_Video_API.as_view())
]
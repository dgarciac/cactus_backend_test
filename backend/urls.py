from django.urls import path

from backend.views.auth import UserAPIView

urlpatterns = [
    path('api/user', UserAPIView.as_view(), name='user'),
]

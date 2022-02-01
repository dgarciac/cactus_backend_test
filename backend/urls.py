from django.urls import path

from backend.views.auth import UserAPIView

urlpatterns = [
    path('', UserAPIView.as_view(), name='user'),
    path('accounts/profile/', UserAPIView.as_view(), name='user'),
]

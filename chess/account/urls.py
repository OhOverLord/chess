from django.urls import path
from .views import RegistrationAPIView, LoginAPIView, refresh_token_view

urlpatterns = [
    path('create/', RegistrationAPIView.as_view(), name='create'),
    path('authenticate/', LoginAPIView.as_view(), name='authenticate'),
    path('refresh_token/', refresh_token_view, name='refresh_token'),
]
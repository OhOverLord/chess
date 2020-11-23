from django.urls import path
from .views import RegistrationAPIView, LoginAPIView

urlpatterns = [
    path('create/', RegistrationAPIView.as_view(), name='create'),
    path('authenticate/', LoginAPIView.as_view(), name='authenticate'),
]
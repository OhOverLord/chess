from django.urls import path
from .views import CreateUserAPIView, authenticate_user

urlpatterns = [
    path('create/', CreateUserAPIView.as_view(), name='create'),
    path('authenticate/', authenticate_user, name='authenticate'),
]
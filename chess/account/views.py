import jwt
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework_jwt.utils import jwt_payload_handler
from rest_framework.decorators import api_view, permission_classes
from .models import User
from .serializers import UserSerializer
from chess.settings import SECRET_KEY


class CreateUserAPIView(APIView):
    permission_classes = (permissions.AllowAny,)
 
    def post(self, request):
        user = request.data
        serializer = UserSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST',])
@permission_classes([permissions.AllowAny,])
def authenticate_user(request):
    try:
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.get(email=email, password=password)
        if user:
            try:
                payload = jwt_payload_handler(user)
                token = jwt.encode(payload, SECRET_KEY)
                user_details = {}
                user_details['name'] = f"{user.first_name} {user.last_name}"
                user_details['token'] = token
                return Response(user_details, status=status.HTTP_200_OK)
            except Exception as e:
                raise e
            else:
                res = {'error': 'can not authenticate with the given credentials or the account has been deactivated'}
            return Response(res, status=status.HTTP_403_FORBIDDEN)
    except KeyError:
        res = {'error': 'please provide a email and a password'}
        return Response(res)
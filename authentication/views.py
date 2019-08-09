from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import CreateUserSerializer, LoginUserSerializer, UserSerializer

# Create your views here.
@api_view(['POST'])
def user_register(request):
    serializer = CreateUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def user_login(request):
    serializer = LoginUserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data
        return Response(UserSerializer(user).data)

    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
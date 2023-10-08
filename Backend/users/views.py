from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view
from .serializers import CustomUserSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser

@api_view(['POST'])
def create_my_CustomUser(request):
    if request.method == 'POST':
        serializer = CustomUserSerializer(data=request.data)
        
        if serializer.is_valid():
            hashed_password = make_password(request.data.get('password'))
            serializer.validated_data['password'] = hashed_password
            serializer.save()  

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_all_my_CustomUsers(request):
        my_CustomUsers = CustomUser.objects.all()

        serializer = CustomUserSerializer(my_CustomUsers, many=True)

        return Response(serializer.data)
        
@api_view(['GET'])
def get_CustomUser_by_id(request, CustomUser_id):
    try:
        CustomUser = CustomUser.objects.get(pk=CustomUser_id)
    except CustomUser.DoesNotExist:
        return Response({'error': 'CustomUser not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = CustomUserSerializer(CustomUser)

    return Response(serializer.data)

@api_view(['PUT', 'PATCH'])
def update_my_CustomUser(request, pk):
    try:
        my_CustomUser = CustomUser.objects.get(pk=pk)
    except CustomUser.DoesNotExist:
        return Response({'error': 'Object not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = CustomUserSerializer(my_CustomUser, data=request.data)
    elif request.method == 'PATCH':
        serializer = CustomUser(my_CustomUser, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save() 
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_my_CustomUser(request, pk):
    try:
        my_CustomUser = CustomUser.objects.get(pk=pk)
    except CustomUser.DoesNotExist:
        return Response({'error': 'Object not found'}, status=status.HTTP_404_NOT_FOUND)

    my_CustomUser.delete()

    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def login_custom_user(request):
    if request.method == 'POST':
        print(request.data)
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user) 
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

    return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .serializers import AccountSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Account
def hello(request):
    return JsonResponse({'message': 'Hello, Django!'})
# Create your views here.

@api_view(['POST'])
def create_my_account(request):
    if request.method == 'POST':
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_all_my_accounts(request):
        my_accounts = Account.objects.all()

        serializer = AccountSerializer(my_accounts, many=True)

        return Response(serializer.data)
@api_view(['GET'])
def get_account_by_id(request, account_id):
    try:
        account = Account.objects.get(pk=account_id)
    except Account.DoesNotExist:
        return Response({'error': 'Account not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = AccountSerializer(account)

    return Response(serializer.data)
@api_view(['PUT', 'PATCH'])
def update_my_account(request, pk):
    try:
        my_account = Account.objects.get(pk=pk)
    except Account.DoesNotExist:
        return Response({'error': 'Object not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = AccountSerializer(my_account, data=request.data)
    elif request.method == 'PATCH':
        serializer = Account(my_account, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save() 
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_my_account(request, pk):
    try:
        my_account = Account.objects.get(pk=pk)
    except Account.DoesNotExist:
        return Response({'error': 'Object not found'}, status=status.HTTP_404_NOT_FOUND)

    my_account.delete()

    return Response(status=status.HTTP_204_NO_CONTENT)
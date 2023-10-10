from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import BudgetEntry
from .serializers import BudgetEntrySerializer

@api_view(['POST'])
def create_budget_entry(request):
    if request.method == 'POST':
        serializer = BudgetEntrySerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_all_budget_entries(request):
    budget_entries = BudgetEntry.objects.all()
    serializer = BudgetEntrySerializer(budget_entries, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_budget_entry_by_id(request, budget_entry_id):
    try:
        budget_entry = BudgetEntry.objects.get(pk=budget_entry_id)
    except BudgetEntry.DoesNotExist:
        return Response({'error': 'BudgetEntry not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = BudgetEntrySerializer(budget_entry)
    return Response(serializer.data)

@api_view(['PUT', 'PATCH'])
def update_budget_entry(request, pk):
    try:
        budget_entry = BudgetEntry.objects.get(pk=pk)
    except BudgetEntry.DoesNotExist:
        return Response({'error': 'BudgetEntry not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = BudgetEntrySerializer(budget_entry, data=request.data)
    elif request.method == 'PATCH':
        serializer = BudgetEntrySerializer(budget_entry, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save() 
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_budget_entry(request, pk):
    try:
        budget_entry = BudgetEntry.objects.get(pk=pk)
    except BudgetEntry.DoesNotExist:
        return Response({'error': 'BudgetEntry not found'}, status=status.HTTP_404_NOT_FOUND)

    budget_entry.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

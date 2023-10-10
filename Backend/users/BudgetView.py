from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Budget
from .serializers import BudgetSerializer

@api_view(['POST'])
def create_budget(request):
    if request.method == 'POST':
        serializer = BudgetSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_all_budgets(request):
    budgets = Budget.objects.all()
    serializer = BudgetSerializer(budgets, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_budget_by_id(request, budget_id):
    try:
        budget = Budget.objects.get(pk=budget_id)
    except Budget.DoesNotExist:
        return Response({'error': 'Budget not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = BudgetSerializer(budget)
    return Response(serializer.data)

@api_view(['PUT', 'PATCH'])
def update_budget(request, pk):
    try:
        budget = Budget.objects.get(pk=pk)
    except Budget.DoesNotExist:
        return Response({'error': 'Budget not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = BudgetSerializer(budget, data=request.data)
    elif request.method == 'PATCH':
        serializer = BudgetSerializer(budget, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save() 
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_budget(request, pk):
    try:
        budget = Budget.objects.get(pk=pk)
    except Budget.DoesNotExist:
        return Response({'error': 'Budget not found'}, status=status.HTTP_404_NOT_FOUND)

    budget.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

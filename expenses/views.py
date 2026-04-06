from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Sum, Avg, Max, Min
from .models import Expense
from .serializers import ExpenseSerializer


from django.contrib.auth.models import User

from django.contrib.auth import logout

from django.contrib.auth import authenticate, login

@api_view(['POST'])
def api_login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({
            "status": "error",
            "message": "Username and password required"
        }, status=400)

    user = authenticate(username=username, password=password)

    if user is None:
        return Response({
            "status": "error",
            "message": "Invalid credentials"
        }, status=401)

    login(request, user)

    return Response({
        "status": "success",
        "message": "Login successful"
    })

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def api_logout(request):
    logout(request)
    return Response({
        "status": "success",
        "message": "Logged out successfully"
    })

@api_view(['POST'])
def api_register(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({"error": "Username and password required"}, status=400)

    if User.objects.filter(username=username).exists():
        return Response({
            "status": "error",
            "message": "User already exists"
        }, status=400)

    user = User.objects.create_user(username=username, password=password)

    return Response({
    "status": "success",
    "message": "User created successfully"
    })

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def api_add_expense(request):
    serializer = ExpenseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_view_expenses(request):
    expenses = Expense.objects.filter(user=request.user)
    serializer = ExpenseSerializer(expenses, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def api_update_expense(request, id):
    expense = Expense.objects.filter(id=id, user=request.user).first()
    if not expense:
        return Response({
        "status": "error",
        "message": "Expense not found"
        }, status=404)
    serializer = ExpenseSerializer(expense, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def api_delete_expense(request, id):
    expense = Expense.objects.filter(id=id, user=request.user).first()
    if not expense:
        return Response({
        "status": "error",
        "message": "Expense not found"
        }, status=404)
    expense.delete()
    return Response({
    "status": "success",
    "message": "Deleted successfully"
    })


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_search_expense(request):
    expenses = Expense.objects.filter(user=request.user)
    q = request.GET.get('q')
    min_amount = request.GET.get('min')
    max_amount = request.GET.get('max')

    if q:
        expenses = expenses.filter(title__icontains=q)
    if min_amount:
        expenses = expenses.filter(amount__gte=min_amount)
    if max_amount:
        expenses = expenses.filter(amount__lte=max_amount)

    serializer = ExpenseSerializer(expenses, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_filter_by_date(request):
    expenses = Expense.objects.filter(user=request.user)
    from_date = request.GET.get('from_date')
    to_date = request.GET.get('to_date')

    if from_date:
        expenses = expenses.filter(date__gte=from_date)
    if to_date:
        expenses = expenses.filter(date__lte=to_date)

    serializer = ExpenseSerializer(expenses, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def home(request):
    return Response({
        "message": "Welcome to Finance Tracker API 🚀",
        "endpoints": {
            "register": "/api/register/",
            "login": "/api/login/",
            "expenses": "/api/expenses/",
            "summary": "/api/summary/",
        }
    })

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_summary(request):
    expenses = Expense.objects.filter(user=request.user)
    total_income = expenses.filter(type='income').aggregate(Sum('amount'))['amount__sum'] or 0
    total_expense = expenses.filter(type='expense').aggregate(Sum('amount'))['amount__sum'] or 0
    balance = total_income - total_expense

    return Response({
    "status": "success",
    "data": {
        "total_income": total_income,
        "total_expense": total_expense,
        "balance": balance
        }
    })


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_monthly_report(request):
    month = request.GET.get('month')
    year = request.GET.get('year')
    expenses = Expense.objects.filter(user=request.user)

    if month and year:
        expenses = expenses.filter(date__month=month, date__year=year)

    total = expenses.aggregate(Sum('amount'))['amount__sum'] or 0
    return Response({"total": total})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_top_5_expenses(request):
    expenses = Expense.objects.filter(user=request.user).order_by('-amount')[:5]
    serializer = ExpenseSerializer(expenses, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_lowest_5_expenses(request):
    expenses = Expense.objects.filter(user=request.user).order_by('amount')[:5]
    serializer = ExpenseSerializer(expenses, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_average_expenses(request):
    avg = Expense.objects.filter(user=request.user).aggregate(Avg('amount'))['amount__avg'] or 0
    return Response({"average": avg})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_max_min_expense(request):
    choice = request.GET.get('choice')
    expenses = Expense.objects.filter(user=request.user)

    if choice == 'max':
        value = expenses.aggregate(Max('amount'))['amount__max'] or 0
        return Response({"max": value})
    elif choice == 'min':
        value = expenses.aggregate(Min('amount'))['amount__min'] or 0
        return Response({"min": value})

    return Response({
    "status": "error",
    "message": "Invalid choice"
    }, status=400)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_category_summary(request):
    expenses = Expense.objects.filter(user=request.user, type='expense')

    data = {}

    for expense in expenses:
        category = expense.category
        data[category] = data.get(category, 0) + expense.amount

    return Response({
        "status": "success",
        "data": data
    })
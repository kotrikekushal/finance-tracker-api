from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('expenses/', views.api_view_expenses),
    path('expenses/add/', views.api_add_expense),
    path('expenses/update/<int:id>/', views.api_update_expense),
    path('expenses/delete/<int:id>/', views.api_delete_expense),

    path('expenses/search/', views.api_search_expense),
    path('expenses/filter/', views.api_filter_by_date),

    path('summary/', views.api_summary),
    path('monthly-report/', views.api_monthly_report),

    path('top-5/', views.api_top_5_expenses),
    path('lowest-5/', views.api_lowest_5_expenses),

    path('average/', views.api_average_expenses),
    path('max-min/', views.api_max_min_expense),

    path('register/', views.api_register),
    path('category-summary/', views.api_category_summary),
    path('login/', views.api_login),
    path('logout/', views.api_logout),
    
]   
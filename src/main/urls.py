

from django.urls import path, include
from .views import main_view, home_view, dashboard_view, employees_list, approve_employee

urlpatterns = [
    path('', main_view, name= 'main'),
    path('home/', home_view, name = 'home'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('dashboard/employees', employees_list, name='employees_list'),
    path('employees/approve/<int:employee_id>/', approve_employee, name='approve_employee'),
    
]
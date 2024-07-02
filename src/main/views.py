from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from users.models import Profile
# Create your views here.
def main_view(request):
    return render(request, 'views/main.html', {})



@login_required
def home_view(request):
    return render(request, "views/home.html", {},)

@login_required
def dashboard_view(request):
    return render(request, "supervisor/dashboard.html", {},)

@login_required
def employees_list(request):
    employees = Profile.objects.all()  # You might want to filter this to exclude supervisors if needed
    return render(request, 'supervisor/employees_list.html', {'employees': employees})

@login_required
def approve_employee(request, employee_id):
    profile = get_object_or_404(Profile, id=employee_id)
    profile.is_verified = True
    profile.save()
    return redirect('employees_list')  # Redirect back to the employees list after approval
# users/views.py
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Profile
from .forms import UserForm, ProfileForm
from main.forms import GreenhouseForm

@login_required
def dashboard(request):
    if request.user.groups.filter(name='Supervisor').exists():
        # User is a supervisor
        return render(request, 'supervisorDashboard.html')
    else:
        # User is not a supervisor
        return render(request, 'views/home.html')

def login_view(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request=request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'You have successfully logged in as {username}')
                # Check if user is in 'Supervisor' group
                if user.groups.filter(name='Supervisors').exists():
                    # Redirect to supervisor dashboard
                    return redirect('dashboard')
                else:
                    # Redirect to home page for regular users
                    return redirect('home')
            else:
                messages.error(request, 'Unable to log in')
        else:
            messages.error(request, 'An error occurred while trying to log in')
    else:
        login_form = AuthenticationForm()

    return render(request, 'views/login.html', {'login_form': login_form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('main')

class RegisterView(View):
    def get(self, request):
        register_form = UserCreationForm()
        return render(request, 'views/register.html', {'register_form': register_form})

    def post(self, request):
        register_form = UserCreationForm(data=request.POST)
        if register_form.is_valid():
            user = register_form.save()
            user.refresh_from_db()
            Profile.objects.create(user=user)  # Create a profile instance
            login(request, user)
            messages.success(request, f'User {user.username} is registered successfully')
            return redirect('home')
        else:
            messages.error(request, 'An error occurred while trying to register')
            return render(request, 'views/register.html', {'register_form': register_form})





@method_decorator(login_required, name='dispatch')
class ProfileView(View):

    def get(self, request):
        
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
        greenhouse_form = GreenhouseForm(instance=request.user.profile.greenhouse)
        return render(request, 'views/profile.html', {'user_form': user_form, 
                                                      'profile_form': profile_form,
                                                      'greenhouse_form': greenhouse_form,
                                                      })
    

    def post(self, request):
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        greenhouse_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile.greenhouse)
        
        if user_form.is_valid() and profile_form.is_valid() and greenhouse_form.is_valid():
            user_form.save()
            profile_form.save()
            greenhouse_form.save()
            messages.success(request, f'Profile Updated Successfuly')
            return redirect('home')

        else: 
            messages.error(request, 'Error occured while Updating Profile')

        return render(request, 'views/profile.html', {'user_form': user_form,
                                                      'greenhouse_form': greenhouse_form, 
                                                      'profile_form': profile_form})
    


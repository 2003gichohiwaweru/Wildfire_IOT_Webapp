
from django.urls import path, include
from .views import login_view, RegisterView, logout_view, view_profile, edit_profile

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', logout_view, name='logout'),
    path('profile/', view_profile, name='profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
]
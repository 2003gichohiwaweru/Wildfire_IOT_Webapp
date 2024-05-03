

from django.urls import path, include
from .views import main_view, home_view,dashboard_view

urlpatterns = [
    path('', main_view, name= 'main'),
    path('home/', home_view, name = 'home'),
    path('supervisor/', dashboard_view, name='supervisor')
]
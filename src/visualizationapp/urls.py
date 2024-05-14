from django.urls import path, include
from .views import temp_data

urlpatterns = [
    
    path('temperature/', temp_data, name= 'temp' )
    
]
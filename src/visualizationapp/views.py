from django.shortcuts import render

# Create your views here.
def temp_data(request):
    return render(request, 'views/temp.html', {})

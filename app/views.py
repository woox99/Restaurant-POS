from django.shortcuts import render, redirect

# Create your views here.
def apps(request):
    return render(request, 'apps.html')
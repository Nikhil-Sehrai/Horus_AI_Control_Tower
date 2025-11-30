from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'home/home.html')

def dashboard(request):
    return render(request, 'home/dashboard.html')

def problem(request):
    return render(request, 'home/problem.html')
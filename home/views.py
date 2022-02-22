# from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from home.models import  accounts

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

# def register(request):
#     return render(request, 'register.html')

def register(request):
    context = {}
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('age') and request.POST.get('address') and request.POST.get('password') and request.POST.get('email') and request.POST.get('mobile'):
            saveRecord = accounts()

            saveRecord.name = request.POST.get('name')
            saveRecord.age = request.POST.get('age')
            saveRecord.address = request.POST.get('address')
            saveRecord.password = request.POST.get('password')
            saveRecord.email = request.POST.get('email')
            saveRecord.mobile = request.POST.get('mobile')

            saveRecord.save()
            return HttpResponse("added successfully !!")

    else:
        return render(request, 'register.html', context)
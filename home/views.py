# from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.
def index(request):
    return render(request, 'index.html')
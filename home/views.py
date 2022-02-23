# from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from home.models import  accounts, msgs
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def ccontact_form(request):
    return render(request, 'contact_form.html')


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
            messages.success(request, 'Acccount Created Successsfully')
            return render(request, 'register.html', context)

    else:
        return render(request, 'register.html', context)


def login(request):
    context = {}
    if request.method == 'POST':
        try:
            userInfo = accounts.objects.get(email=request.POST.get('email'))
            if (request.POST.get('password') == (userInfo.password)):
                request.session['email'] = userInfo.email
                return redirect('home')
            else:
                messages.error(request, 'Incorrect Password...!')
        except accounts.DoesNotExist as e:
            messages.error(request, 'No user found...!')

    return render(request, 'login.html', context)


def contact_form(request):
    if request.method == 'POST':
        # user = accounts.objects.get(email=request.session['email'])
        if request.POST.get('person_name') and request.POST.get('person_email') and request.POST.get('person_contact') and request.POST.get('msg'):
            user = msgs()
            user.person_name = request.POST.get('person_name')
            user.person_email = request.POST.get('person_email')
            user.person_contact = request.POST.get('person_contact')
            user.msg = request.POST.get('msg')

            user.save()
            messages.success(request, 'We Have Received Your Massage')
            return redirect('contact_form')
    else:
        return render(request, 'contact_form.html',)
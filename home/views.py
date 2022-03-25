# from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from home.models import  accounts, msgs
from django.contrib import messages
from django.db import connection

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def contact_form(request):
    return render(request, 'contact_form.html')

def view_profile(request):
    user = accounts.objects.get(email=request.session['email'])
    acc = accounts.objects.raw( 'SELECT * FROM users WHERE email = %s', [user.email] )
    return render(request, 'view_profile.html', {'acc': acc, 'user': user})

def edit_profile(request):
    return render(request, 'edit_profile.html')

def home(request):
    return render(request, 'home.html')  


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
            messages.success(request, 'Thanks for contacting us!')
            return redirect('contact_form')
    else:
        return render(request, 'contact_form.html',)

def userindex(request):
    return render(request, 'userindex.html')

def edit_profile(request):
    return render(request, 'edit_profile.html')

def search(request):
    return render(request, 'search.html')

def doctorslist(request):
    return render(request, 'doctorslist.html')
def quizform(request):
    if request.method == 'POST':
        #  if request.POST.get('ques1') and request.POST.get('ques2') and request.POST.get('ques3') and request.POST.get('ques4') and request.POST.get('ques5') and request.POST.get('ques6') and request.POST.get('ques7') and request.POST.get('ques8') :
            # print("hii")
            q1= request.POST.get('ques1')
            
            q2= request.POST.get('ques2')
           
            q3= request.POST.get('ques3')
            q4= request.POST.get('ques4')
            q5= request.POST.get('ques5')
            q6= request.POST.get('ques6')
            q7= request.POST.get('ques7')
            q8= request.POST.get('ques8')
            # print(q1)
            # print(q2)
            # print(q3)
            
            # print(q4)  
           
            # print(q5)
            
            # print(q6)
           
            # print(q7)
            # print(q8)
            
            if q1=='1' and q2== '5' and q3== '9' and q4 == '13' and q5== '17' and q6=='37' and q7=='28' and q8=='32':
                messages.success(request, 'you are suffering from anxiety')
                return redirect('result')
            elif q1=='2' and q2== '6' and q3== '10' and q4 == '14' and q5== '18' and q6=='21' and q7=='29' and q8=='33':
                messages.success(request, 'you are suffering from panic attack')
                return redirect('result')
            elif q1=='3' and q2== '5' and q3== '11' and q4 == '13' and q5== '20' and q6=='24' and q7=='28' and q8=='34':
                messages.success(request, 'you are suffering from OCD')
                return redirect('result')
            elif q1=='4' and q2== '5' and q3== '9' and q4 == '13' and q5== '17' and q6=='40' and q7=='30' and q8=='32':
                messages.success(request, 'you are suffering from stress')
                return redirect('result')
            else:
                messages.success(request, 'you are suffering from deppression')
                return redirect('result')
    return render(request, 'quizform.html') 

def result(request):
    return render(request, 'result.html')  

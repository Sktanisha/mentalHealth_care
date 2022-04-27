# from django.shortcuts import render
import profile
import uuid
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from home.models import  accounts, msgs,chat,docaccounts,quizresult
from home.models import  Profile, accounts, msgs, docaccounts
from django.contrib import messages
from django.db import connection

from mentalHealth_care.helpers import send_forget_password_mail

# Create your views here.
def index(request):
    return render(request, 'index.html')




def view_profile(request):
    user = accounts.objects.get(email=request.session['email'])
    acc = accounts.objects.raw( 'SELECT * FROM users WHERE email = %s', [user.email] )
    return render(request, 'view_profile.html', {'acc': acc, 'user': user})



def edit_profile(request):
    if request.method == 'POST':
        user = accounts.objects.get(email=request.session['email'])
        if request.POST.get('editName') and request.POST.get('editAge') and request.POST.get('editMobile') and request.POST.get('editAddress'):

            user.name = request.POST.get('editName')
            user.age = request.POST.get('editAge')
            user.mobile = request.POST.get('editMobile')
            user.address = request.POST.get('editAddress')
            user.save()
            messages.success(
                request, "User details updated successfully...!")

            return redirect('edit_profile')
    else:
        try:
            user = accounts.objects.get(email=request.session['email'])
            return render(request, 'edit_profile.html', {'user': user})
        except:
            messages.error(request, 'You need to login first')
            return redirect('login')

def home(request):
    return render(request, 'home.html')  

def userindex(request):
    return render(request, 'userindex.html') 

def docregister(request):
    return render(request, 'docregister.html') 

def feedback(request):
    return render(request, 'feedback.html') 


def register(request):
    context = {}
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('age') and request.POST.get('address') and request.POST.get('password') and request.POST.get('email') and request.POST.get('mobile'):
            saveRecord = accounts()
            saveToken = Profile()

            saveRecord.name = request.POST.get('name')
            saveRecord.age = request.POST.get('age')
            saveRecord.address = request.POST.get('address')
            saveRecord.password = request.POST.get('password')
            saveRecord.email = request.POST.get('email')
            saveRecord.mobile = request.POST.get('mobile')
   
            saveRecord.save()
            saveToken.user = saveRecord
            saveToken.save()
            messages.success(request, 'Acccount Created Successsfully')
            return render(request, 'register.html', context)

    else:
        return render(request, 'register.html', context)

def docregister(request):
    context = {}
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('title') and request.POST.get('birth') and request.POST.get('gender') and request.POST.get('nid')  and request.POST.get('age') and request.POST.get('address') and request.POST.get('password') and request.POST.get('email') and request.POST.get('mobile'):
            saveDoc = docaccounts()

            saveDoc.doc_title = request.POST.get('title')
            saveDoc.doc_name = request.POST.get('name')
            saveDoc.doc_age = request.POST.get('age')
            saveDoc.doc_gender = request.POST.get('gender')
            saveDoc.doc_nid = request.POST.get('nid')
            saveDoc.doc_address = request.POST.get('address')
            saveDoc.doc_password = request.POST.get('password')
            saveDoc.doc_email = request.POST.get('email')
            saveDoc.doc_mobile = request.POST.get('mobile')
            saveDoc.doc_birth = request.POST.get('birth')
   
            saveDoc.save()
            messages.success(request, 'Acccount Created Successsfully')
            return render(request, 'docregister.html', context)

    else:
        return render(request, 'docregister.html', context)


def docregister(request):
    context = {}
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('title') and request.POST.get('birth') and request.POST.get('gender') and request.POST.get('nid') and request.POST.get('age') and request.POST.get('address') and request.POST.get('password') and request.POST.get('email') and request.POST.get('mobile'):
            saveDoc = docaccounts()

            saveDoc.doc_title = request.POST.get('title')
            saveDoc.doc_name = request.POST.get('name')
            saveDoc.doc_age = request.POST.get('age')
            saveDoc.doc_gender = request.POST.get('gender')
            saveDoc.doc_nid = request.POST.get('nid')
            saveDoc.doc_address = request.POST.get('address')
            saveDoc.doc_password = request.POST.get('password')
            saveDoc.doc_email = request.POST.get('email')
            saveDoc.doc_mobile = request.POST.get('mobile')
            saveDoc.doc_birth = request.POST.get('birth')
   
            saveDoc.save()
            messages.success(request, 'Acccount Created Successsfully')
            return render(request, 'docregister.html', context)

    else:
        return render(request, 'docregister.html', context)


def login(request):
    context = {}
    if request.method == 'POST':
        try:
            userInfo = accounts.objects.get(email=request.POST.get('email'))
            if (request.POST.get('password') == (userInfo.password)):
                request.session['email'] = userInfo.email
                return redirect('userindex')
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
    if request.method == 'POST':
        user = accounts.objects.get(email=request.session['email'])
        if request.POST.get('editName') and request.POST.get('editAge') and request.POST.get('editMobile') and request.POST.get('editAddress'):

            user.name = request.POST.get('editName')
            user.age = request.POST.get('editAge')
            user.mobile = request.POST.get('editMobile')
            user.address = request.POST.get('editAddress')
            user.save()
            messages.success(
                request, "User details updated successfully...!")

            return redirect('edit_profile')
    else:
        try:
            user = accounts.objects.get(email=request.session['email'])
            return render(request, 'edit_profile.html', {'user': user})
        except:
            messages.error(request, 'You need to login first')
            return redirect('login')

def quizform(request):
    if request.method == 'POST':
        #  if request.POST.get('ques1') and request.POST.get('ques2') and request.POST.get('ques3') and request.POST.get('ques4') and request.POST.get('ques5') and request.POST.get('ques6') and request.POST.get('ques7') and request.POST.get('ques8') :
            # print("hii")
            save = quizresult()
            save.name = request.POST.get('email')
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
                save.result = 'anxiety'
                messages.success(request, 'You Are Facing A Minor Inconvenience. In Medical Terms It Is called anxiety')
                
                return redirect('result')
            elif q1=='2' and q2== '6' and q3== '10' and q4 == '14' and q5== '18' and q6=='21' and q7=='29' and q8=='33':
                messages.success(request, 'You Are Facing A Minor Inconvenience. In Medical Terms It Is called panic attack')
                save.result = 'panic attack'
                return redirect('result')
            elif q1=='3' and q2== '5' and q3== '11' and q4 == '13' and q5== '20' and q6=='24' and q7=='28' and q8=='34':
                messages.success(request, 'You Are Facing A Minor Inconvenience. In Medical Terms It Is called OCD')
                save.result = 'OCD'
                return redirect('result')
            elif q1=='4' and q2== '5' and q3== '9' and q4 == '13' and q5== '17' and q6=='40' and q7=='30' and q8=='32':
                messages.success(request, 'You Are Facing A Minor Inconvenience. In Medical Terms It Is called stress')
                save.result = 'stress'
                return redirect('result')
            else:
                messages.success(request, 'You Are Facing A Minor Inconvenience. In Medical Terms It Is called Depression')
                save.result = 'depression'
                return redirect('result')

            
    return render(request, 'quizform.html') 

def result(request):
    return render(request, 'result.html')  

def information(request):
    if request.method == 'POST':
        room = request.POST['room']
        get_room = chat.objects.filter(room_name=room)
        if get_room:
            c = get_room[0]
            number = c.allowed_users
            if int(number) < 2:
                number = 2
                return redirect(f'/video/{room}/join/')
        else:
            create = chat.objects.create(room_name=room,allowed_users=1)
            if create:
                return redirect(f'/video/{room}/created/')
    return render(request,'information.html')

def video(request,room,created):
    return render (request,'video.html',{'created':created, 'room':room})
def blog(request):
    return render(request, 'blog.html')

def blog1(request):
    return render(request, 'blog1.html')

def blog2(request):
    return render(request, 'blog2.html')

def blog3(request):
    return render(request, 'blog3.html')

def blog4(request):
    return render(request, 'blog4.html')

def blog5(request):
    return render(request, 'blog5.html')

def blog6(request):
    return render(request, 'blog6.html')

def blog7(request):
    return render(request, 'blog7.html')

def blog8(request):
    return render(request, 'blog8.html')

def blog9(request):
    return render(request, 'blog9.html')
def reset_password(request):
    try:
        if request.method == 'POST' and request.POST.get('resetEmail'):
            email = request.POST.get('resetEmail')

        if not accounts.objects.filter(email=email).first():
            # messages.error(request, 'No user found with this email.')
            return HttpResponse("No user found with this email.")

        user_obj = accounts.objects.get(email=email)
        token = str(uuid.uuid4())
        profile_obj = Profile.objects.get(user=user_obj.id)
        profile_obj.forget_password_token = token
        profile_obj.save()
        send_forget_password_mail(user_obj.email, token)
        return HttpResponse("An email is sent.")

    except Exception as e:
        print(e)
        return render(request, 'reset_password/forget-password.html')

def change_password(request, token):
    context = {}

    try:
        profile_obj = profile.objects.filter(
            forget_password_token=token).first()
        context = {'user_id': profile_obj.user.id}

        if request.method == 'POST':
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('reconfirm_password')
            user_id = request.POST.get('user_id')

            if user_id is None:
                return HttpResponse("No user id found.")

            if new_password != confirm_password:
                return HttpResponse("Booth password should be equal")

            user_obj = accounts.objects.filter(id=user_id).first()
            user_obj.password = new_password
            user_obj.save()
            return HttpResponse("Password updated successfully!!")
        else:
            return render(request, 'reset_password/change-password.html', context)

    except Exception as e:
        print(e)
        return HttpResponse("url has already been used.")

from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),   
    path('register', views.register, name='register'),
    path('contact_form', views.contact_form, name='contact_form'),
    path('view_profile', views.view_profile, name='view_profile'),
    path('edit_profile', views.edit_profile, name='edit_profile'),
    path('home', views.home, name='home'),
    path('userindex', views.userindex, name='userindex'),
    path('quizform', views.quizform, name='quizform'),
    path('result', views.result, name='result'),
    path('docregister', views.docregister, name='docregister'),
    path('feedback', views.feedback, name='feedback'),
	path('reset-password', views.reset_password, name='reset-password'),
    path('change-password/<token>/', views.change_password, name='change-password'),
]
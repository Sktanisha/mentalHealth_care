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
    path('blog', views.blog, name='blog'),
    path('blog1', views.blog1, name='blog1'),
    path('blog2', views.blog2, name='blog2'),
    path('blog3', views.blog3, name='blog3'),
    path('blog4', views.blog4, name='blog4'),
    path('blog5', views.blog5, name='blog5'),
    path('blog6', views.blog6, name='blog6'),
    path('blog7', views.blog7, name='blog7'),
    path('blog8', views.blog8, name='blog8'),
    path('blog9', views.blog9, name='blog9'),
]
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),   
    path('register', views.register, name='register'),
    path('contact_form', views.contact_form, name='contact_form'),
    path('view_profile', views.view_profile, name='view_profile'),
    path('edit_profile', views.edit_profile, name='edit_profile'),
]
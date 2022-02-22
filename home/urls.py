from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),   
    path('register', views.register, name='register'),
    path('contuct_us', views.contuct_us, name='contuct_us'),
]
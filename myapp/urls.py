from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='signup'),
    path('login', views.userlogin, name='login'),
    path('logout', views.userlogout, name='logout'),
    path('home', views.home, name='home'),
    path('scheduler', views.scheduler, name='scheduler'),

]

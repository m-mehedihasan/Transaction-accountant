from django.urls import path
from . import views

urlpatterns = [
 path('', views.home, name='home'),
 path('home', views.home, name='home'),
 path('login', views.login, name='login'),
 path('sign_up', views.sign_up, name='sign_up'),
 path('logout', views.logout, name='logout'),
 path('profile', views.profile, name='profile'),
 path('service', views.service, name='service'),
 path('update', views.update, name='update'),
]


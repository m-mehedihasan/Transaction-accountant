from django.shortcuts import render, redirect
from myapp.forms import UsersForm
from django.http import *
from datetime import datetime as dt

def home(request):
	title = 'Transaction Accountant || Home'
	template_name = 'index.html'
	now = dt.now()
	time = now.strftime("%H:%M:%S")
	request.session['time'] = time
	return render(request, template_name, {'title':title})

def login(request):
	form = UsersForm()
	template_name = 'login.html'
	return render(request, template_name, {'form':form})


def sign_up(request):
	
	form = UsersForm()
	template_name = 'sign_up.html'
	return render(request, template_name, {'form': form})



#END

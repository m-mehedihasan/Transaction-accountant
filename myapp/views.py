from django.shortcuts import render, redirect
from myapp.forms import UsersForm
from django.http import *
from datetime import datetime as dt
from django.contrib import messages


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
	context = {'form':form}
	return render(request, template_name, context)


def sign_up(request):
	template_name = 'sign_up.html'
	if request.method == 'POST':
		form = UsersForm(request.POST)
		if form.is_valid():
			password = request.POST.get('password')
			confirm_password = request.POST.get('confirm_password')
			if password == confirm_password:
				try:
					form.save()
					message = 'Account created successfully!'
					messages.success(request, message)
				except:
					message = 'Account creation failed! Try after few minutes!'
					messages.error(request, message)
					pass
				return redirect('/login')
			else:
				messages.error(request, 'Both password should be match.')
				form = UsersForm(request.POST)
				context = {'form':form}
				return render(request, template_name, context)

	else:
		form = UsersForm()
		context = {'form':form}
		return render(request, template_name, context)

def owner(request):
	template_name = 'owner.html'
	return render(request, template_name)
#END

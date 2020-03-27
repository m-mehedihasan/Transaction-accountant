from django.shortcuts import render, redirect
from myapp.forms import UsersForm
from django.http import *
from datetime import datetime as dt
from django.contrib import messages
from .models import Users

def home(request):
	title = 'Transaction Accountant || Home'
	template_name = 'index.html'
	now = dt.now()
	time = now.strftime("%H:%M:%S")
	request.session['time'] = time
	context = {'title': title}
	return render(request, template_name, context)

def login(request):
	template_name = 'login.html'
	if request.method == 'POST':
		objects = Users.objects.all()
		form = UsersForm(request.POST)
		if request.POST.get('login'):
			data = request.POST.copy()
			username = data.get('username')
			password = data.get('password')
			for object in objects:
				if username == object.username and password == object.password:
					request.session['username'] = username
					return redirect('/home')
			else:
				message = 'Username or password is incorrect!'
				messages.error(request, message)
				form = UsersForm(request.POST)
				context = {'form':form}
				return render(request, template_name, context)
	else:
		form = UsersForm()
		context = {'form':form}
		return render(request, template_name, context)


def sign_up(request):
	template_name = 'sign_up.html'
	condition = False
	is_user_exist = False

	if request.method == 'POST':
		form = UsersForm(request.POST)
		if form.is_valid():
			password = request.POST.get('password')
			confirm_password = request.POST.get('confirm_password')
			username = request.POST.get('username')
			try:
				objects = Users.objects.all()
				for object in objects:
					if username == object.username: #check if username already
						is_user_exist = True        #taken or not
			except:
				pass

			if password == confirm_password and is_user_exist == False:
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
				if password != confirm_password:
					message = 'Both password should be matched.'
				else:
					message = 'Username already taken!'

				messages.error(request, message)
				form = UsersForm(request.POST)
				context = {'form':form}
				return render(request, template_name, context)

	else:
		form = UsersForm()
		context = {'form':form}
		return render(request, template_name, context)


def logout(request):
	try:
		del request.session['username']
	except KeyError:
		pass
	return redirect('/home')

def profile(request):
	context = {}
	template_name = 'profile.html'
	try:
		user = Users.objects.get(username = request.session['username'])
		context['user'] = user
		name = user.first_name + ' ' + user.last_name
		context['title'] = 'TA PROFILE: ' + name
		ta_id = (user.first_name + '.' + user.last_name + '_' + str(user.id)).lower()
		context['ta_id'] = ta_id
		context['name'] = name
		form = UsersForm(Users.objects.get(username = request.session['username']))
		context['form'] = form
		return render(request, template_name, context)
	except:
		return redirect('/home')
		pass	


def service(request):
	context = {}
	message = 'Should edit'
	messages.info(request, message)
	return redirect('/profile')

def update(request):
	return redirect('/home')
#END

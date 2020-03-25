from django.shortcuts import render, redirect

def home(request):
	title = 'Transaction Accountant || Home'
	template_name = 'index.html'
	return render(request, template_name, {'title':title})

#END

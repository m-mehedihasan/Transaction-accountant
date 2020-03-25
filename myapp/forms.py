from django import forms
from myapp.models import Users

class UsersForm(forms.ModelForm):
	class Meta:
		model = Users
		widgets = {
		'first_name': forms.TextInput(attrs={'placeholder':'Enter your First Name'}),
		'last_name': forms.TextInput(attrs={'placeholder':'Enter your Last Name'}),
		'username': forms.TextInput(attrs={'placeholder':'Enter a username'}),
		'password': forms.TextInput(attrs={'placeholder':'Enter a password'}),
		'confirm_password': forms.TextInput(attrs={'placeholder':'Re-enter the password'}),
		'contact_no': forms.TextInput(attrs={'placeholder':'Enter your contact number'}),
		'password': forms.PasswordInput(),
		'confirm_password': forms.PasswordInput(),
		
		}
		fields = "__all__"


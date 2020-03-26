from django import forms
from myapp.models import Users

class UsersForm(forms.ModelForm):
	class Meta:
		model = Users
		widgets = {
		'first_name': forms.TextInput(attrs={'placeholder':'Enter your First Name'}),
		'last_name': forms.TextInput(attrs={'placeholder':'Enter your Last Name'}),
		'username': forms.TextInput(attrs={'placeholder':'Enter a username', 'type': 'email'}),
		'password': forms.TextInput(attrs={'placeholder':'Enter a password', 'type': 'password'}),
		'confirm_password': forms.TextInput(attrs={'placeholder':'Re-enter the password', 'type': 'password'}),
		'contact_no': forms.TextInput(attrs={'placeholder':'Enter your contact number'}),
		
		}
		fields = "__all__"


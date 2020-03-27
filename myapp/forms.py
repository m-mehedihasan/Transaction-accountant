from django import forms
from myapp.models import Users

class UsersForm(forms.ModelForm):
	class Meta:
		model = Users
		widgets = {
		'first_name': forms.TextInput(attrs={'placeholder':'Enter your First Name', 'class':'form-control'}),
		'last_name': forms.TextInput(attrs={'placeholder':'Enter your Last Name', 'class':'form-control'}),
		'username': forms.TextInput(attrs={'placeholder':'Enter a username', 'type': 'email', 'class':'form-control'}),
		'password': forms.TextInput(attrs={'placeholder':'Enter a password', 'type': 'password', 'class':'form-control'}),
		'confirm_password': forms.TextInput(attrs={'placeholder':'Re-type your password', 'type': 'password', 'class':'form-control'}),
		'contact_no': forms.TextInput(attrs={'placeholder':'Enter your contact number', 'class':'form-control'}),
		
		}
		fields = "__all__"


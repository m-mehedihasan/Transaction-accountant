from django import forms
from myapp.models import Users, TransactionList

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
		

class UsersFormShow(forms.ModelForm):
	class Meta:
		model = Users
		widgets = {
		'first_name': forms.TextInput(attrs={'placeholder':'First Name', 'class':'form-control', 'disabled': 'true'}),
		'last_name': forms.TextInput(attrs={'placeholder':'Last Name', 'class':'form-control', 'disabled': 'true'}),
		'username': forms.TextInput(attrs={'placeholder':'Your username', 'type': 'email', 'class':'form-control', 'disabled': 'true'}),
		'password': forms.TextInput(attrs={'placeholder':'Your password', 'type': 'password', 'class':'form-control', 'disabled': 'true'}),
		'confirm_password': forms.TextInput(attrs={'placeholder':'Re-type your password', 'type': 'password', 'class':'form-control', 'disabled':'true'}),
		'contact_no': forms.TextInput(attrs={'placeholder':'Your Contact No', 'class':'form-control', 'disabled': 'true'}), 
		
		}
		fields = "__all__"


class TransactionListForm(forms.ModelForm):
	class Meta:
		model = TransactionList
		widgets = {
		'provider_name': forms.TextInput(attrs={'placeholder':'Provider name',
		 'class':'form-group form-control text-capitalize', }),
		'receiver_name': forms.TextInput(attrs={'placeholder':'Receiver name',
		 'class':'form-group form-control text-capitalize', }),
		'amount': forms.TextInput(attrs={'placeholder':'Amount',
		                         'type':'number', 'step':'0.01', 'min':'0', 'class':'form-control',}),
		'paid': forms.TextInput(attrs={'placeholder':'Paid',
		                         'type':'number', 'step':'0.01', 'min':'0', 'class':'form-control', }),
		'date': forms.TextInput(attrs={'type':'date', 'class':'form-control', 'placeholder': 'DD/MM/YYYY', }),
		}
		fields = [
		'provider_name',
		 'receiver_name',
		 'amount',
		 'paid',
		 'date',
		]
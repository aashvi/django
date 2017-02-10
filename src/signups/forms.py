from django import forms

from .models import SignUp, Customer

class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp

class CustomerForm(forms.ModelForm):
	class Meta:
		model = Customer


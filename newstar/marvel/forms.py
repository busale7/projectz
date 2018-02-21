from django import forms

from .models import Captain #importing the class Business from models.py
from django.contrib.auth.models import User


class LoginForm(forms.Form):
	username = forms.CharField(required=True)
	password = forms.CharField(required=True, widget=forms.PasswordInput())
	

class UserRegistrationForm(forms.ModelForm):
	class Meta :
		model=User 
		fields =['username','email','first_name','last_name','password']
		widgets= {
			"password": forms.PasswordInput()
		}

class CaptainForm(forms.ModelForm) :
	class Meta:
		model= Captain
		fields ='__all__'
		#['name', 'release_date', 'platforms', 'multiplayer', 'image']

		
		widgets= {
			"add_date" : forms.DateInput(attrs={"type": "date"})

		}
		
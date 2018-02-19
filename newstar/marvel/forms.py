from django import forms

from .models import Captain #importing the class Business from models.py

class CaptainForm(forms.ModelForm) :
	class Meta:
		model= Captain
		fields ='__all__'

		
		widgets= {
			"add_date" : forms.DateInput(attrs={"type": "date"})

		}
		
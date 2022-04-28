from django import forms
from .models import *

class EmployerForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = '__all__'
        

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('firstname', 'lastname')
        

class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'
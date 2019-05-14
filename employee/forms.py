from django import forms

from .models import Employee

class GetForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('first_name', 'last_name','email','birth_date','designation')

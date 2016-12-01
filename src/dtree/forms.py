from django import forms
from django.contrib.auth.models import User


from .models import DataSet


class DataSetForm(forms.ModelForm):

    class Meta:
        model = DataSet
        fields = ['dataSetName', 'dmName']
        labels = {'dataSetName': ('Data Set Name'),
                  'dmName': ('Data Managers Name'),}
        
class AddLdsIdForm(forms.ModelForm):

    class Meta:
        model = DataSet
        fields = ['ldsId']
        labels = {'ldsId': ('LDS id'),}

class AuditForm(forms.Form):
    date_from = forms.DateField(label='Date from (dd/mm/yy)', input_formats=['%d/%m/%y'])
    date_to = forms.DateField(label='Date to (dd/mm/yy)', input_formats=['%d/%m/%y'])
    email = forms.CharField(label='Email', max_length=100)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        
        
        

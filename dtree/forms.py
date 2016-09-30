from django import forms


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
    date_from = forms.DateField(label='date from', input_formats=['%d/%m/%y'])
    date_to = forms.DateField(label='date to', input_formats=['%d/%m/%y'])
    email = forms.CharField(label='email', max_length=100)




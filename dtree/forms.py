from django import forms
from django.contrib.auth.models import User

from .models import DataSet


class DataSetForm(forms.ModelForm):

    class Meta:
        model = DataSet
        fields = ['dataSetName']

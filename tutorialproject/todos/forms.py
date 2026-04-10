from django import forms

class PersonForm(forms.Form):
    name = forms.CharField(max_length=100,required=True,label='your name')
    age = forms.IntegerField(label='your age')
    job = forms.CharField(max_length=100,required=False,label='your job')

from django import forms

class DataForm(forms.Form):
    input_data = forms.CharField()
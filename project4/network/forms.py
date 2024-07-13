from django import forms

class new_post(forms.Form):
    text = forms.CharField(label='text', max_length=1000)
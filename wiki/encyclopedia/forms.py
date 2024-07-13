from django import forms

class SearchBar(forms.Form):
    SearchInput = forms.CharField(label="Search Encyclopedia")


class NewPage(forms.Form):
    Title = forms.CharField(label="Page Title")
    textarea = forms.CharField(label="Page Text", max_length=500, widget=forms.Textarea(attrs={'name':'body', 'rows':3, 'cols':5}))

class EditPage(forms.Form):
    textarea = forms.CharField(label="Page Text", max_length=500, widget=forms.Textarea(attrs={'name':'body', 'rows':3, 'cols':5}))

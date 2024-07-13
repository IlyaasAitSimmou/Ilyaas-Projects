from django import forms
from .models import *

class comment(forms.Form):
    comment = forms.CharField(label='comment', max_length=1000)

class NewListing(forms.Form):
    listing = forms.CharField(label="Auction name", max_length=64)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label="Category", to_field_name="categoryName")
    description = forms.CharField(label="Description", max_length=300, widget=forms.Textarea(attrs={'name':'description', 'rows':1, 'cols':5}))
    imageUrl = forms.CharField(label="Auction Image URL", max_length=1000)
    price = forms.FloatField()

class PlaceBid(forms.Form):
    bid = forms.FloatField(label="Set Bid")
    


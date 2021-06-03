
from django import forms


class BasicForm(forms.Form):
	name = forms.CharField()
	email = forms.EmailField()
	text = forms.CharField(widget = forms.Textarea)

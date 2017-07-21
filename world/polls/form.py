from django import forms

class nameform(forms.Form):
    your_name=forms.CharField(label='your name' ,max_length=100)
class Postform(forms.Form):
    content=forms.CharField(max_length=100)
    created=forms.DateTimeField()
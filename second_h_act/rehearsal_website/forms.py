from django import forms

class form(forms.Form):
    sceneNum = forms.IntegerField
    character = forms.IntegerField
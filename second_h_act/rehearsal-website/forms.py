from django import forms

class RehearsalForm(forms.Form):
    sceneNum = forms.IntegerField(label='sceneNum')
    #character = forms.IntegerField(label='character')

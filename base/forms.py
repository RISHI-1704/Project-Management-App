from django import forms
from .models import Tasks

class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = '__all__'
        widgets = {
            'users':forms.CheckboxSelectMultiple()
        }
        
class RemoveUser(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['users']
        widgets = {
            'users':forms.CheckboxSelectMultiple()
        }        
        
class TaskEdit(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['name','description','users']
        widgets = {
            'users':forms.CheckboxSelectMultiple()
        }

class ConfirmPass(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput())
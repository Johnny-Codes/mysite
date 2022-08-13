from django import forms

from .models import toDo

class toDoForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Title'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Description'}))
    class Meta:
        model = toDo
        fields = "__all__"
from django import forms
from ..models import Designation


class AddDesignationForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'autofocus': True}))
    class Meta:
        model = Designation
        fields = ('id', 'name')
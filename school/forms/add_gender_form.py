from django import forms
from ..models import Gender


class AddGenderForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'autofocus': True}))
    class Meta:
        model = Gender
        fields = ('id', 'name')
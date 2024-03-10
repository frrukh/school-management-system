from django import forms
from ..models import Timing

class AddTimingForm(forms.ModelForm):
    period_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    period_from = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}))
    period_to = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}))

    class Meta:
        model = Timing
        fields = ('__all__')
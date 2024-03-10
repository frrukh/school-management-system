from django import forms
from ..models import ClassAndTiming, Staff, Subject, Grade, Timing


class AddClassAndTimingForm(forms.ModelForm):
    class_name = forms.ModelChoiceField(queryset=Grade.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    period_one = forms.ModelChoiceField(queryset=Timing.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    period_one_subject = forms.ModelChoiceField(queryset=Subject.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    period_one_teacher = forms.ModelChoiceField(required=False, queryset=Staff.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    period_two = forms.ModelChoiceField(queryset=Timing.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    period_two_subject = forms.ModelChoiceField(queryset=Subject.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    period_two_teacher = forms.ModelChoiceField(required=False, queryset=Staff.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    period_three = forms.ModelChoiceField(queryset=Timing.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    period_three_subject = forms.ModelChoiceField(queryset=Subject.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    period_three_teacher = forms.ModelChoiceField(required=False, queryset=Staff.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    period_four = forms.ModelChoiceField(queryset=Timing.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    period_four_subject = forms.ModelChoiceField(queryset=Subject.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    period_four_teacher = forms.ModelChoiceField(required=False, queryset=Staff.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    period_five = forms.ModelChoiceField(queryset=Timing.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    period_five_subject = forms.ModelChoiceField(queryset=Subject.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    period_five_teacher = forms.ModelChoiceField(required=False, queryset=Staff.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    period_six = forms.ModelChoiceField(queryset=Timing.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    period_six_subject = forms.ModelChoiceField(queryset=Subject.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    period_six_teacher = forms.ModelChoiceField(required=False, queryset=Staff.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    period_seven = forms.ModelChoiceField(queryset=Timing.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    period_seven_subject = forms.ModelChoiceField(queryset=Subject.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    period_seven_teacher = forms.ModelChoiceField(required=False, queryset=Staff.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    status = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'form-check-input'}), initial=True)

    class Meta():
        model = ClassAndTiming
        fields = ('__all__')
from django import forms
from ..models import Staff, Gender, Designation, Subject, EmploymentStatus


class AddStaffForm(forms.ModelForm):
    first_name = forms.CharField(max_length=75, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(required=False, max_length=75, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=75, widget=forms.TextInput(attrs={'class': 'form-control'}))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    dob = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type':'date'}))
    gender = forms.ModelChoiceField(queryset=Gender.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    qualification = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'})) 
    experience = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'form-control'})) 
    designation = forms.ModelChoiceField(queryset=Designation.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    subject = forms.ModelChoiceField(queryset=Subject.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    emergency_phone = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    joining_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type':'date'}))
    salary = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    employment_status = forms.ModelChoiceField(queryset=EmploymentStatus.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    contract_details = forms.CharField(max_length=1000, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    status = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input d-none'}), initial=True, label='')
    password1 = forms.CharField(max_length=30, initial='ooppeenn123', label='', widget=forms.TextInput(attrs={'class': 'form-control d-none'}))
    password2 = forms.CharField(max_length=30, initial='ooppeenn123', label='', widget=forms.TextInput(attrs={'class': 'form-control d-none'}))
    is_staff = forms.BooleanField(initial=True, widget=forms.CheckboxInput(attrs={'class': 'form-check-input d-none'}), label='')

    class Meta:
        model = Staff
        fields = ('__all__')

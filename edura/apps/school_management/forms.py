from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'first_name', 
            'last_name', 
            'birth_date', 
            'gender', 
            'academic_level', 
            'enrollment_status', 
            'photo'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter first name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter last name'
            }),
            'birth_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'gender': forms.RadioSelect(
                attrs={'class': 'custom-radio-buttons'}
            ),
            'academic_level': forms.Select(
                attrs={'class': 'form-select'}
            ),
            'enrollment_status': forms.Select(
                attrs={'class': 'form-select'}
            ),
            'photo': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }

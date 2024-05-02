from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_number', 'first_name', 'last_name', 'email', 'field_of_study', 'cgpa']
        labels = {
            'student_number': 'Student Number',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'field_of_study': 'Field of Study',
            'cgpa': 'CGPA',
        }

        widgets = {
            'student_number': forms.NumberInput(attrs={'required': True, 'maxlength': 10}),
            'first_name': forms.TextInput(attrs={'required': True}),
            'last_name': forms.TextInput(attrs={'required': True}),
            'email': forms.EmailInput(attrs={'required': True}),
            'field_of_study': forms.TextInput(attrs={'required': True}),
            'cgpa': forms.NumberInput(attrs={'min': 0.0, 'max': 5.0, 'step': 0.01}),
        }

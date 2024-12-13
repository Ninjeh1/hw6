from django import forms
from .models import *

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'lastname', 'age', 'course']

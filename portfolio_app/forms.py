from django import forms
from .models import Portfolio, Student

# If you have a Portfolio model, you'd create a PortfolioForm like this:
class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['title', 'contact_email']# list all the fields you want to include in your form

# If you need to create a form for the Student model, it would look similar:
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'major', 'email','Portfolio']  # again, list all the fields for the form


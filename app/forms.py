from django import forms
from app.models import Todo

class StudentForm(forms.Form):
    name = forms.CharField(max_length=50, min_length=3, label="Student's Name", help_text="Enter The Name Of Student")
    age = forms.IntegerField(max_value=20, min_value=10)


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'status', 'category']
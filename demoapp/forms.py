from django.db.models import fields
from django.forms import ModelForm
from .models import Books, Student

class StudentForm(ModelForm):
    class Meta:
        model=Student
        fields='__all__'

class BooksForm(ModelForm):
    class Meta:
        model=Books
        fields='__all__'
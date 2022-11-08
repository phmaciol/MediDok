import django_filters
from django import forms

from  Pacjent.models import *
from  Terminarz.models import *

class Visit_filters(django_filters.FilterSet):
    term = forms.DateField(widget=forms.DateInput(attrs={"class": "form-control"}))
    class Meta:
         model = Visit
         fields = ['term',]
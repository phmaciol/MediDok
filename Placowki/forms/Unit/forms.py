from django.forms import ModelForm, modelformset_factory
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User
from Placowki.models import *
from Regiony.models import *
from django.core import validators
from django.forms import CharField
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin



class UnitALLforms(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Nazwa zakładu", }),
                           label='Nazwa Jednostki:')
    organization = forms.ModelChoiceField(queryset=Struct_Organization.objects.all(), widget=forms.Select(attrs={"class": "form-control"}), label="Zakład leczniczy")
    logo = forms.FileField(widget=forms.FileInput(attrs={"class": "form-control"}), label="Logo jednostkileczniczego", required=False)


    class Meta:
        model = Unit
        fields = '__all__'




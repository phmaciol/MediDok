from django.forms import ModelForm, modelformset_factory
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User
from Placowki.models import *
from Regiony.models import *
from django.core import validators
from django.forms import CharField
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
PLACE_TYPE = (
    ('0', ('Poradnia ogólna')),
    ('1', ('Poradnia Specjalistyczna')),
    ('2', ('Szpitale')),

)
DEKL = (
    ('0', ('TAK')),
    ('1', ('NIE')),

)








class ZakladFormALL(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Nazwa zakładu", }),
                           label='Nazwa zakładu leczniczego:')
    organization = forms.ModelChoiceField(queryset=Organization.objects.all(),widget=forms.Select(attrs={"class": "form-control", "placeholder": "Nazwa Podmiotu", }), label='Nazwa podi leczniczego ')
    city = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Miasto", }),
                           label='Miasto; ', max_length=30)
    adress1 = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Ulica", }),
                              label='Ulica: ', max_length=20)
    adress2 = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Numer budynku", }),
                              label='Numer budynku: ', max_length=10)
    adress3 = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Numer", }),
                              label='Numer: ', max_length=5)
    phone = forms.CharField(widget=forms.NumberInput(
        attrs={"class": "form-control", "placeholder": "Numer telefonu", 'oninput': 'limit_input_two()',
               'id': 'phone_field'}), label='Numer telefonu: ')
    mail = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "E-mail", }),
                            label='E-mail: ')
    type_place = forms.ChoiceField(
        widget=forms.Select(attrs={"class": "form-control", "placeholder": "Typ placówki", }), label='Typ placówki:',
        choices=PLACE_TYPE)
    dekl = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-control", "id": "option", "name": "options", }),
                             initial=1, label='Czy wymagana deklaracja:', choices=DEKL)
    logo = forms.FileField(widget=forms.FileInput(attrs={"class": "form-control"}), label="Logo Zakładu leczniczego", required=False)

    class Meta:
        model = Struct_Organization
        fields = '__all__'




# class ZakladFormEditPodmiot(forms.ModelForm):
#     name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Nazwa zakładu", }),
#                            label='Nazwa zakładu leczniczego:')
#     # organization = forms.CharField(widget=forms.Select(attrs={"class": "form-control", "placeholder": "Nazwa zakładu", }), label='Nazwa zakładu leczniczego ')
#     city = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Miasto", }),
#                            label='Miasto; ', max_length=30)
#     adress1 = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Ulica", }),
#                               label='Ulica: ', max_length=20)
#     adress2 = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Numer budynku", }),
#                               label='Numer budynku: ', max_length=10)
#     adress3 = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Numer", }),
#                               label='Numer: ', max_length=5)
#     phone = forms.CharField(widget=forms.NumberInput(
#         attrs={"class": "form-control", "placeholder": "Numer telefonu", 'oninput': 'limit_input_two()',
#                'id': 'phone_field'}), label='Numer telefonu: ')
#     mail = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "E-mail", }),
#                             label='E-mail: ')
#     type_place = forms.ChoiceField(
#         widget=forms.Select(attrs={"class": "form-control", "placeholder": "Typ placówki", }), label='Typ placówki:',
#         choices=PLACE_TYPE)
#     dekl = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-control", "id": "option", "name": "options", }),
#                              initial=1, label='Czy wymagana deklaracja:', choices=DEKL)
#     logo = forms.FileField(widget=forms.FileInput(attrs={"class": "form-control"}), label="Logo Zakładu leczniczego", required=False)
#
#     class Meta:
#         model = Struct_Organization
#         fields = ('name', 'city', 'adress1', 'adress2', 'adress3', 'phone', 'mail', 'type_place', 'dekl', 'logo')



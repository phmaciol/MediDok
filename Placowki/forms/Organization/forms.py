from django.forms import ModelForm, modelformset_factory
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User
from Placowki.models import *
from Regiony.models import *
from django.core import validators
from django.forms import CharField
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin


class PodmiotForms(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Nazwa podmiotu", }),
                           label='Nazwa podmiotuy leczniczego ')
    nip = forms.CharField(widget=forms.NumberInput(
        attrs={"class": "form-control", "placeholder": "Nip podmiotu", 'oninput': 'limit_input()', "id": "nip"}),
                          label='Numer NIP podmiotu ')
    regon = forms.CharField(widget=forms.NumberInput(
        attrs={"class": "form-control", "placeholder": "Regon podmiotu", 'oninput': 'limit_input()', "id": "regon"}),
                            label='Numer REGON podmiotu ')
    krs = forms.CharField(widget=forms.NumberInput(
        attrs={"class": "form-control", "placeholder": "KRS podmiotu", 'oninput': 'limit_input()', "id": "krs"}),
                          label='Numer KRS podmiotu')
    number_resort = forms.CharField(
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Numer resortowy"}),
        label='Numer księgi resortowej')
    number_swiat = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Numer świadczeniodawcy"}),
        label='Numer świadczeniodawcy')
    oddz_nfz = forms.ModelChoiceField(queryset=NFZ.objects.all(), widget=forms.Select(
        attrs={"class": "form-control", "placeholder": "Numer świadczeniodawcy"}), label='Numer świadczeniodawcy')
    logo = forms.FileField(widget=forms.FileInput(attrs={"class": "form-control", "placeholder": "brak pliku z logo"}),
                           label='Logo')

    class Meta:
        model = Organization
        fields = "__all__"

        def __init__(self):
            self.cleaned_data = None

        def clean(self):
            super(PodmiotForms, self).clean()

            nip = self.cleaned_data.get('nip')
            regon = self.cleaned_data.get('regon')
            krs = self.cleaned_data.get('krs')

            if (len(nip) < 10):
                self._errors['nip'] = self.error_class([
                    'Nip składa się z 10 cyfr!'
                ])

            if len(regon) < 9:
                self._errors['regon'] = self.error_class([
                    'Regon składa się z 9 cyfr!'
                ])
            if (len(krs) < 10):
                self._errors['krs'] = self.error_class([
                    'KRS składa się z 10 cyfr!'
                ])

            return self.cleaned_data


class PodmiotEditForms(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Nazwa podmiotu", }),
                           label='Nazwa podmiotuy leczniczego ')
    nip = forms.CharField(widget=forms.NumberInput(
        attrs={"class": "form-control", "placeholder": "Nip podmiotu", 'oninput': 'limit_input()', "id": "nip_Edit"}),
                          label='Numer NIP podmiotu ')
    regon = forms.CharField(widget=forms.NumberInput(
        attrs={"class": "form-control", "placeholder": "Regon podmiotu", 'oninput': 'limit_input()',
               "id": "regon_edit"}), label='Numer REGON podmiotu ')
    krs = forms.CharField(widget=forms.NumberInput(
        attrs={"class": "form-control", "placeholder": "KRS podmiotu", 'oninput': 'limit_input()', "id": "krs_edit"}),
                          label='Numer KRS podmiotu')
    number_resort = forms.CharField(
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Numer resortowy"}),
        label='Numer księgi resortowej')
    number_swiat = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Numer świadczeniodawcy"}),
        label='Numer świadczeniodawcy')
    oddz_nfz = forms.ModelChoiceField(queryset=NFZ.objects.all(), widget=forms.Select(
        attrs={"class": "form-control", "placeholder": "Numer świadczeniodawcy"}), label='Numer świadczeniodawcy')

    # logo = forms.FileField(widget=forms.FileInput(attrs={"class": "form-control", "placeholder": "brak pliku z logo"}), label='Logo')
    class Meta:
        model = Organization
        fields = "__all__"


PLACE_TYPE = (
    ('0', ('Poradnia ogólna')),
    ('1', ('Poradnia Specjalistyczna')),
    ('2', ('Szpitale')),

)
DEKL = (
    ('0', ('TAK')),
    ('1', ('NIE')),

)


class ZakladFormPodmiot(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Nazwa zakładu", }),
                           label='Nazwa zakładu leczniczego:')
    # organization = forms.CharField(widget=forms.Select(attrs={"class": "form-control", "placeholder": "Nazwa zakładu", }), label='Nazwa zakładu leczniczego ')
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

    def __init__(self, pk, *args, **kwargs):
        super(ZakladFormPodmiot, self).__init__(*args, **kwargs)
        self.fields['organization'].queryset = Organization.objects.filter(id=pk)
        self.fields['organization'].widget.attrs['class'] = 'form-control'


class ZakladFormEditPodmiot(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Nazwa zakładu", }),
                           label='Nazwa zakładu leczniczego:')
    # organization = forms.CharField(widget=forms.Select(attrs={"class": "form-control", "placeholder": "Nazwa zakładu", }), label='Nazwa zakładu leczniczego ')
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
        fields = ('name', 'city', 'adress1', 'adress2', 'adress3', 'phone', 'mail', 'type_place', 'dekl', 'logo')




class UnitFormPodmiot(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Nazwa zakładu", }),
                           label='Nazwa Jednostki:')
    logo = forms.FileField(widget=forms.FileInput(attrs={"class": "form-control"}), label="Logo jednostkileczniczego", required=False)


    class Meta:
        model = Unit
        fields = '__all__'

    def __init__(self, pk, *args, **kwargs):
        super(UnitFormPodmiot, self).__init__(*args, **kwargs)
        self.fields['organization'].queryset = Struct_Organization.objects.filter(id=pk)
        self.fields['organization'].widget.attrs['class'] = 'form-control'

class UnitEditForms(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Nazwa zakładu", }),
                           label='Nazwa Jednostki:')
    logo = forms.FileField(widget=forms.FileInput(attrs={"class": "form-control"}), label="Logo jednostkileczniczego", required=False)


    class Meta:
        model = Unit
        fields = '__all__'

    def __init__(self, pk, *args, **kwargs):
        super(UnitEditForms, self).__init__(*args, **kwargs)
        self.fields['organization'].queryset = Struct_Organization.objects.filter(id=pk)
        self.fields['organization'].widget.attrs['class'] = 'form-control'

class UnitEditForms(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Nazwa zakładu", }),
                           label='Nazwa zakładu leczniczego:')

    class Meta:
        model = Unit
        fields = ('name',)
class DoctorFormADD(forms.ModelForm):
    name = forms.ModelChoiceField(queryset=Personal_med.objects.filter(groupadd__name='lekarz'), widget=forms.Select(attrs={}))

    class Meta:
        model = doctor
        fields = ('name', 'unit')

    def __init__(self, pk, *args, **kwargs):
        super(DoctorFormADD, self).__init__(*args, **kwargs)
        self.fields['unit'].queryset = Unit.objects.filter(id=pk)

from django import forms
from django.contrib.auth.models import User
from django.db.models import Q

from Pacjent.models import *
from Placowki.models import *
from Terminarz.models import *
from Profile.models import *
from Slowniki.models import *










class DEKLFORMS(forms.ModelForm):

    idunit = forms.ModelChoiceField( queryset = Unit.objects.filter(organization__type_place=0), widget=forms.Select(attrs={"class": "form-control"}), label="Jednostka",)
    # idpac = forms.CharField( widget=forms.TextInput(attrs={"class": "form-control"}), label="Pacjent", disabled=True, required=False)
    # iddoc = forms.CharField( widget=forms.TextInput(attrs={"class": "form-control"}), label="Lekarz", disabled=True,  required=False)
    # idfield = forms.CharField( widget=forms.TextInput(attrs={"class": "form-control"}), label="Dokument złożony przez pacjenta", disabled=True,  required=False)


    class Meta:
        model = dekl
        fields= ('idunit',)

class EDITDEKLFORMS(forms.ModelForm):

        class Meta:
                model = dekl
                fields = ('iddoc',)
class FORM_PERS(forms.ModelForm):
    class Meta:
        model = Form_all
        fields = '__all__'
class FORM_PLACE(forms.ModelForm):
    unity = forms.ModelChoiceField(queryset=Unit.objects.all(), widget=forms.Select(attrs={"class": "form-control"}), label="Wybierz placówkę")
    class Meta:
        model = Visit
        fields = ('unity',)
class TERM_VISIT(forms.ModelForm):

    class Meta:
        model = doctor
        fields = ('name',)
class REST_VISIT(forms.ModelForm):
    patient_person = forms.ModelChoiceField(queryset=Personal.objects.all() ,widget=forms.Select(attrs={"class": "form-control pers"}), label="Pacjent")

    class Meta:
        model = Visit
        fields = ('patient_person' , 'unity' , 'term', 'key', 'status', 'confirmation', 'type_visit', 'description')

    def __init__(self, pk, pi, *args, **kwargs):
        super(REST_VISIT, self).__init__(*args, **kwargs)
        self.fields['unity'].queryset = Unit.objects.filter(id=pk)
        self.fields['unity'].widget.attrs['class'] = 'form-control unit'
        self.fields['term'].queryset = Term_day.objects.filter(Q(work_place=pk) and Q(work_person=pi))
        self.fields['term'].widget.attrs['class'] = 'form-control term'
        self.fields['key'].widget.attrs['class'] = 'form-control'
        self.fields['status'].widget.attrs['class'] = 'form-control'
        self.fields['confirmation'].widget.attrs['class'] = 'form-control'
        self.fields['type_visit'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'



class EDITPROFILE(forms.ModelForm):
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class": 'form-control'}), label="Nazwisko", required=False)
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class": 'form-control'}), label="Imię", required=False)
    pesel = forms.CharField(widget=forms.NumberInput(attrs={"class": 'form-control'}), label="Pesel", required=False)
    npwz = forms.CharField(widget=forms.NumberInput(attrs={"class": 'form-control'}), label="Numer prawa wykonywania zawodu", required=False)
    date_brith = forms.DateField(widget=forms.DateInput(attrs={"class": 'form-control'}), label="Data urodzin", required=False)
    phone = forms.CharField(widget=forms.DateInput(attrs={"class": 'form-control'}), label="Numer telefonu", required=False)
    class Meta:
        model = Personal_med
        fields = ('last_name', 'first_name', 'pesel', 'npwz', 'date_brith', 'phone')

class FORMREC(forms.ModelForm):
    class Meta:
        model = e_system_RECEPTY
        fields = ('key_e',)
class FORMSKIER(forms.ModelForm):
    class Meta:
        model = e_system_SKIEROWANIA
        fields = ('key_e',)

class DOCFORM(forms.ModelForm):
    id10 = forms.ModelChoiceField(queryset=ICD10.objects.all(),widget=forms.SelectMultiple(attrs={"id": "choices-multiple-remove-button", "placeholedr": "Wpisz 5 liter"}), label="Rozpozania")
    class Meta:
        model = Visit
        fields = ('id10',)
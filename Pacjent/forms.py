from django import forms
from django.contrib.auth.models import User
from Pacjent.models import *
from Slowniki.models import *



class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('name', 'doc')

class VisitForm_CUST(forms.ModelForm):

    patient_user = forms.ModelChoiceField( queryset = User.objects.all(), widget=forms.Select(attrs={"class": "form-control"}), label="Użytkownik")
    patient_person = forms.ModelChoiceField(queryset= Personal.objects.all(), widget=forms.Select(attrs={"class": "form-control"}), label="Pesel")
    unity = forms.ModelChoiceField( queryset=Unit.objects.all(), widget=forms.Select(attrs={"class": "form-control"}), label="Jednostka lecznicza")
    struct = forms.ModelChoiceField( queryset=Struct_Organization.objects.all(), widget=forms.Select(attrs={"class": "form-control"}), label="Zakład leczniczy")
    organization = forms.ModelChoiceField(queryset=Organization.objects.all(), widget=forms.Select(attrs={"class": "form-control"}), label="Podmiot leczniczy")
    key = forms.CharField(widget=forms.NumberInput(attrs={"class": "form-control"}), label="Kod e-skierowania")

    description = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "Opisz w jakim celu rejestrujesz się do lekarza"}), label="OPIS")


    class Meta:
        model = Visit
        fields= ( 'patient_user' ,'patient_person', 'organization', 'struct','unity', 'description', 'key' )

class VisitForm_EDIT_PAC(forms.ModelForm):

    class Meta:
        model = Visit
        fields= ( 'term', )
    def __init__(self, unitpk, personid, *args, **kwargs):
        super(VisitForm_EDIT_PAC, self).__init__(*args, **kwargs)

        self.fields['term'].queryset = Term_day.objects.filter(work_place=unitpk, work_person=personid)

class DEKLFORM(forms.ModelForm):
    FORM_TYPE = (
        ('0', ('Deklaracja do Lekarza')),
    )
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}), label="Nazwa formularza")
    type_forms = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-control"}), choices=FORM_TYPE ,label="Typ formularza")
    remarks_user = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control"}), label="Opis pacjenta")
    file = forms.FileField(widget=forms.FileInput(attrs={"class": "form-control"}), label="Formularz")
    class Meta:
        model = Form_user
        fields = ('name',  'type_forms', 'remarks_user', 'file' )
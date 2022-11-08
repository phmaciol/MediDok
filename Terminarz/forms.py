from django.forms import ModelForm
from django import forms
from Profile.models import *
from Regiony.models import *
from Placowki.models import *
from .models import *
from django.utils import timezone, dateformat

class GenericTERM(forms.ModelForm):
    WORK = (
        ('0', ('Lekarz')),
        ('1', ('Pielęgniarka')),
        ('2', ('Położna')),
    )
    DAY = (
        (0, ('Poniedziałek')),
        (1, ('Wtorek')),
        (2, ('Środa')),
        (3, ('Czwartek')),
        (4, ('Piątek')),
        (5, ('Sobota')),
        (6, ('Niedziela')),
    )
    TIMEE = (
        ('00:00', "00:00"),
        ('00:30', "00:30"),
        ('01:00', "01:00"),
        ('01:30', "01:30"),
        ('02:00', "02:00"),
        ('02:30', "02:30"),
        ('03:00', "03:00"),
        ('03:30', "03:30"),
        ('04:00', "04:00"),
        ('04:30', "04:30"),
        ('05:00', "05:00"),
        ('05:30', "05:30"),
        ('06:00', "06:00"),
        ('06:30', "06:30"),
        ('07:00', "07:00"),
        ('07:30', "07:30"),
        ('08:00', "08:00"),
        ('08:30', "08:30"),
        ('09:00', "09:00"),
        ('09:30', "09:30"),
        ('10:00', "10:00"),
        ('10:30', "10:30"),
        ('11:00', "11:00"),
        ('11:30', "11:30"),
        ('12:00', "12:00"),
        ('12:30', "12:30"),
        ('13:00', "13:00"),
        ('13:30', "13:30"),
        ('14:00', "14:00"),
        ('14:30', "14:30"),
        ('15:00', "15:00"),
        ('15:30', "15:30"),
        ('16:00', "16:00"),
        ('16:30', "16:30"),
        ('17:00', "17:00"),
        ('17:30', "17:30"),
        ('18:00', "18:00"),
        ('18:30', "18:30"),
        ('19:00', "19:00"),
        ('19:30', "19:30"),
        ('20:00', "20:00"),
        ('20:30', "20:30"),
        ('21:00', "21:00"),
        ('21:30', "21:30"),
        ('22:00', "22:00"),
        ('22:30', "22:30"),
        ('23:00', "23:00"),
        ('23:30', "23:30"),

    )
    TIMEWORK = (
        (5, ("5 minut")),
        (10, ("10 minut")),
        (15, ("15 minut")),
        (20, ("20 minut")),
        (30, ("30 minut")),
    )

    work_place = forms.ModelChoiceField(queryset=Unit.objects.all(), widget=forms.Select(attrs={"class": "form-control"}), label="Jednostka:")
    work_person = forms.ModelChoiceField(queryset=Personal_med.objects.all(), widget=forms.Select(attrs={"class": "form-control"}), label="Personel:")
    work_type = forms.ChoiceField(choices=WORK, widget=forms.Select(attrs={"class": "form-control"}), label="Typ Terminarza:")
    work_day = forms.ChoiceField(choices=DAY, widget=forms.Select(attrs={"class": "form-control"}), label="Terminarz na dzień:")
    work_start = forms.TimeField(widget=forms.NumberInput(attrs={"class": "form-control", "type": "time"}), initial="08:00", label="Godzina rozpoczęcia:")
    work_stop = forms.TimeField( widget=forms.NumberInput(attrs={"class": "form-control", "type": "time"}),initial="15:00", label="Godzina zakończenia:")
    work_time = forms.ChoiceField(choices=TIMEWORK, widget=forms.Select(attrs={"class": "form-control"}) , label="Czas wizyty:")
    work_start_date = forms.DateField( widget=forms.NumberInput(attrs={"class": "form-control", 'type': 'date'}), label="Data rozpoczęcia terminarz:")
    work_stop_date = forms.DateField( widget=forms.NumberInput(attrs={"class": "form-control", 'type': 'date'}), label="Data zakończania terminarz:")
    work_date = forms.DateField( widget=forms.DateInput(attrs={"class": "form-control"}), required=False , initial=timezone.now , label="Data aktualna:")



    class Meta:
        model = Term
        fields = '__all__'



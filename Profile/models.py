from django.db import models
from django.contrib.auth.models import User, Group
from Regiony.models import *
from django.utils import timezone, dateformat

# Create your models here.







class Personal(models.Model):

    NAMEID = (
        ('0', ("Brak")),
        ('1', ("EKUZ")),
        ('2', ("Dowód osobisty")),
        ('3', ("Paszport")),

              )
    PESELANS = (
        ('0', ('TAK')),
        ('1', ('NIE')),
    )


    last_name = models.CharField("Nazwisko", max_length=100,null=True)
    first_name = models.CharField("Imiona", max_length=100,null=True)
    iduser = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date_brith = models.DateField("Data Urodzenia")
    pesel = models.CharField("Pesel", max_length=11, unique=False, null=False)
    peselN = models.CharField("Brak peselu", max_length=11, unique=False, null=True, choices=PESELANS, default=0)
    IDname = models.CharField("Nazwa dokumentu", max_length=100, unique=False, null=True, choices=NAMEID)
    IDnumber = models.CharField("Numer dokumentu", max_length=20, unique=False, null=True)
    phone = models.CharField("Numer telefonu", max_length=9, unique=True, null=True)
    regional_woj = models.ForeignKey(Regional, on_delete=models.PROTECT, null=False, verbose_name=('Województwo') )
    # regional_pow = models.ForeignKey(Powiat, on_delete=models.PROTECT, null=False, verbose_name=('Powiat') )
    regional_city = models.CharField("Miasto", max_length=200, null=True)
    post = models.CharField("Kod Pocztowy", max_length=100, null=False, default=00-000)
    str_name = models.CharField("Ulica", max_length=20, null=False)
    str_number = models.CharField("Numer domu",max_length=4, null=False)
    str_number_one = models.CharField("Numer mieszkania(opcjonalnie)", max_length=4, null=False)
    doc = models.FileField("Skan dowodu", null=False, blank=False)
    check = models.BooleanField("Potwierdzenie konta", null=False, default=False)
    Register_date = models.DateField(default=timezone.now)
    def __str__(self):
        return (self.last_name +" "+ self.first_name +" "+ self.pesel)
    class Meta:
        verbose_name_plural = "Pacjenci"
# ------------------------------------------------
class Personal_med(models.Model):
    # GROUPADD = (
    #     ('2', 'lekarz'),
    #     ('3', 'pielegniarka'),
    #     ('4', 'rejstrator'),
    # )

    last_name = models.CharField("Nazwisko", max_length=100, null=True)
    first_name = models.CharField("Imiona", max_length=100, null=True)
    iduser = models.ForeignKey( User, on_delete=models.CASCADE, unique=True, null=True)
    pesel = models.CharField("Pesel", max_length=11, unique=True, null=True)
    date_brith = models.DateField("Data Urodzenia")
    npwz = models.CharField("Numer prawa wykonywania zawodu", max_length=8,  unique=True, null=False)
    phone = models.CharField("Numer telefonu", max_length=9, unique=True, null=True)
    regional_woj = models.ForeignKey(Regional, on_delete=models.PROTECT, null=True)
    regional_city = models.CharField("Miasto", max_length=200, null=True)
    str_name = models.CharField("Ulica",max_length=20 , null=True)
    str_number = models.CharField("Numer domu", max_length=4, null=True)
    str_number_one = models.CharField("Numer mieszkania(opcjonalnie)",max_length=4, null=True)
    groupadd = models.ForeignKey(Group, on_delete=models.PROTECT, verbose_name="Grupa", null=True)
    Register_date = models.DateField(default=timezone.now)
    def __str__(self):
        return (self.last_name +" "+ self.first_name +" "+ self.pesel +" "+ self.npwz)
    class Meta:
        verbose_name_plural = "Personel"
# ------------------------------------------------

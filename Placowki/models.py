from django.db import models
from Regiony.models import *
from Profile.models import *

# Create your models here.

class NFZ(models.Model):
    name = models.CharField("Oddział NFZ", max_length=200, unique=True, null=True)
    regional = models.ForeignKey(Regional, on_delete=models.PROTECT, null=True, verbose_name="Województwo")
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Oddział NFZ"

class Organization(models.Model):
    name = models.CharField("Nazwa Podmiot Leczniczy", max_length=100, unique=True, null=True)
    nip = models.CharField("Nip podmiotu leczniczego", max_length=10, unique=True, null=True)
    regon = models.CharField("Regon podmiotu leczniczego", max_length=9, unique=True, null=True)
    krs = models.CharField("KRS podmiotu leczniczego", max_length=25, unique=True, null=True)
    number_resort =  models.CharField("Numer księgi resortowej", max_length=25, unique=True, null=True)
    number_swiat = models.CharField("Numer świadczniodawcy", max_length=25, unique=True, null=True)
    oddz_nfz = models.ForeignKey(NFZ, on_delete=models.PROTECT, null=True, verbose_name="Oddział NFZ")
    logo = models.ImageField("Logo", null=True, blank=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Podmiot Leczniczy"


class Struct_Organization(models.Model):
    PLACE_TYPE = (
        ('0', ('Poradnia ogólna')),
        ('1', ('Poradnia Specjalistyczna')),
        ('2', ('Szpitale')),

    )
    DEKL = (
        ('0', ('TAK')),
        ('1', ('NIE')),


    )

    name = models.CharField("Nazwa strukty organizacyjnej", max_length=200, null=False)
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT, null=False, verbose_name="Podmiot leczniczy")
    city = models.CharField("Miasto", max_length=200, null=False)
    adress1 = models.CharField("Ulica", max_length=100, null=False)
    adress2 = models.CharField("Numer domu", max_length=5, null=False)
    adress3 = models.CharField("Numer mieszkania", max_length=5, null=False)
    phone = models.CharField("Telefon", max_length=15, null=False, blank=False)
    mail = models.EmailField("E-mail", max_length=100, null=False, blank=False)
    logo = models.ImageField("Logo", null=False, blank=False)
    type_place = models.CharField("Typ Placówki", max_length=200, null=False, choices=PLACE_TYPE)
    dekl = models.CharField("Czy wymagana delaracja ", max_length=200, null=False, choices=DEKL)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Zakład leczniczy"


class Unit(models.Model):
    name = models.CharField("Nazwa jednostki", max_length=200, null=True)
    organization = models.ForeignKey(Struct_Organization, on_delete=models.PROTECT, null=True, verbose_name="Zakład leczniczy")
    # personel = models.ManyToManyField(Personal_med, verbose_name="Lekarze")

    logo = models.ImageField("Logo", null=True, blank=True)
    def __str__(self):
        struct = self.organization.name
        orga = self.organization.organization.name
        return 'Jednostka ' + self.name + ' Zakład '  + struct + ' Podmiot ' + orga

    class Meta:
        verbose_name_plural = "Jednostka"

class doctor(models.Model):
    first_name = models.CharField("Imię", max_length=100)
    last_name = models.CharField("Nazwisko", max_length=100)
    name = models.ForeignKey(Personal_med, on_delete=models.PROTECT)
    unit = models.ForeignKey(Unit, on_delete=models.PROTECT)

    def __str__(self):
        return self.first_name +" "+ self.last_name

    class Meta:
        verbose_name_plural = "Jednostki i Personel"
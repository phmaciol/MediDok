from django.db import models
from django.contrib.auth.models import *
from Placowki.models import *
from Profile.models import *
from Terminarz.models import *
from Slowniki.models import *
# Create your models here.


class Document(models.Model):
    name = models.CharField("Nazwa", max_length=100, null=True, unique=True)
    author_user = models.ForeignKey(User, on_delete=models.PROTECT, null=True, verbose_name="Użytkownik")
    author_person = models.ForeignKey(Personal, on_delete=models.PROTECT, null=True, verbose_name="Pacjent")
    doc = models.FileField("Załącznik", null=True, blank=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Dokumenty"

class Visit(models.Model):
    STATUS = (
        ('0', ('Niepotwierdzony')),
        ('1', ('Potwierdzony')),

    )
    STATUS_AC = (
        ('0', ('Zarejestrowana')),
        ('1', ('Zapalnowana')),
        ('2', ('Do realizacji')),
        ('3', ('Zrealizowana')),
        ('4', ('Odwołana')),

    )
    VISIT_TYPE = (
        ('0', ('Receptowa')),
        ('1', ('Porada')),
        ('2', ('Teleporada')),
        ('3', ('Z skierowaniem')),
        ('4', ('Kontynuacja')),
        ('5', ('')),


    )
    patient_user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    patient_person = models.ForeignKey(Personal, on_delete=models.PROTECT, null=True)
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT, null=True, verbose_name="Komórka Organizacyjna")
    struct = models.ForeignKey(Struct_Organization, on_delete=models.PROTECT, null=True, verbose_name="Zakład leczniczy")
    unity = models.ForeignKey(Unit, on_delete=models.PROTECT, null=True, verbose_name="Jednostka ")
    term = models.ForeignKey(Term_day, on_delete=models.CASCADE, unique=True, null=True, verbose_name="Data Wizyty ")
    key = models.CharField("Kod e-skierowania", max_length=4, null=True)
    id10 = models.ManyToManyField(ICD10, verbose_name="Rozpoznania", null=True)
    description = models.TextField("Opis", null=True)
    description_person = models.TextField("Opis lekarza", null=True)
    status = models.CharField("Status aktualny", max_length=100, null=True, choices=STATUS_AC, default='0')
    confirmation = models.CharField("Potwierdzenie wizyty", max_length=100,
                                    choices=STATUS, default='0', null=True)
    type_visit = models.CharField("Rodzajy Wizyty", max_length=100,
                                    choices=VISIT_TYPE, default='5')
    dateregister = models.DateField(default=timezone.now)




    class Meta:
        verbose_name_plural = "Wizyty"

class e_system_SKIEROWANIA(models.Model):
    key_e = models.CharField("Kod skierowania", max_length=4, null=True, blank=True, unique=True)
    idvisit = models.ForeignKey(Visit, on_delete=models.PROTECT, verbose_name="Wizyta")
    idpac = models.ForeignKey(Personal, on_delete=models.PROTECT, verbose_name="Pacjents")
    iddoc = models.ForeignKey(Personal_med, on_delete=models.PROTECT, verbose_name="Lekarz")

    def __str__(self):
        return (self.key_e)

    class Meta:
        verbose_name_plural = "Skierowania"
class e_system_RECEPTY(models.Model):
    key_e = models.CharField("Kod Recepty", max_length=4, null=True, blank=True, unique=True)
    idvisit = models.ForeignKey(Visit, on_delete=models.PROTECT, verbose_name="Wizyta")
    idpac = models.ForeignKey(Personal, on_delete=models.PROTECT, verbose_name="Pacjents")
    iddoc = models.ForeignKey(Personal_med, on_delete=models.PROTECT, verbose_name="Lekarz")

    def __str__(self):
        return (self.key_e)

    class Meta:
        verbose_name_plural = "Recepty"

class Form_all(models.Model):

     name = models.CharField("Nazwa Formularza do pobrania", max_length=100, null=True, blank=True)
     file = models.FileField("Fromularz do pobrania", null=True, blank=True)

     def __str__(self):
         return (self.name)
     class Meta:
         verbose_name_plural = "Formularze"


class Form_user(models.Model):

    FORM_TYPE = (
        ('0', ('Deklaracja do Lekarza')),
        ('1', ('Deklaracja do Pielęgniarki środowiskowej')),
        ('2', ('Deklaracja do Położnej')),
        ('3', ('Formularz zdrowotny COVID')),
    )
    STAUS = (
        ('0', ('Przesłany')),
        ('1', ('W trakcie weryfikacji')),
        ('2', ('Zakceptowany')),
        ('3', ('Niezakceptowany')),

    )
    name = models.CharField("Nazwa przesłanego Formularza ", max_length=100, null=True, blank=True)
    patient_person = models.ForeignKey(Personal, on_delete=models.PROTECT, null=True, verbose_name="Pacjent")
    # medical = models.ForeignKey(Personal_med, on_delete=models.PROTECT, null=True, verbose_name="Personel")
    type_forms = models.CharField("Rodzaj Formularza", max_length=100, null=True, choices=FORM_TYPE)
    status = models.CharField("Status dokumentu", max_length=100, null=True, choices=STAUS, default=0)
    remarks_user = models.TextField("Uwagi użytkownika", null=True)
    remarks_person = models.TextField("Uwagi Pracownika placówki", null=True)
    name_unit = models.ForeignKey(Unit, on_delete=models.PROTECT, verbose_name="Jednostka", null=True)
    publish_date = models.DateField("Data przesłania", default=timezone.now)
    file = models.FileField("Fromularz do pobrania", null=True, blank=True)

    def __str__(self):
        return (self.name)
    class Meta:
        verbose_name_plural = "Formularze przesłane przez użytkownika"
class dekl(models.Model):

    idpac = models.ForeignKey(Personal, on_delete=models.CASCADE, unique=True, null=True, verbose_name="Pacjent")
    iddoc = models.ForeignKey(Personal_med, on_delete=models.CASCADE, unique=True, null=True, verbose_name="Lekarz")
    idunit = models.ForeignKey(Unit, on_delete=models.CASCADE, verbose_name="Jednostka")
    idfield = models.ForeignKey(Form_user, on_delete=models.CASCADE, unique=True, null=True, verbose_name="Formularz")

    class Meta:
        verbose_name_plural = "Deklaracje"
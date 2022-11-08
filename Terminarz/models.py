from django.db import models
from Placowki.models import *
from Profile.models import *
from django.utils import timezone, dateformat
# Create your models here.
class Term(models.Model):
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

    work_place = models.ForeignKey(Unit, on_delete=models.PROTECT, null=True, verbose_name="Jednostka")
    work_person = models.ForeignKey(Personal_med, on_delete=models.PROTECT, null=True, verbose_name="Osoba personelu")
    work_type = models.CharField("Typ terminarza", max_length=100, choices=WORK, null=True)
    work_start = models.TimeField(auto_now=False, auto_now_add=False, verbose_name="Początek wizyty")
    work_stop = models.TimeField(auto_now=False, auto_now_add=False, verbose_name="Koniec wizyty")
    work_day = models.IntegerField("Dzień tygodnia", null=True, choices=DAY)
    work_time = models.IntegerField("Czas trwania wizyty", null=True)
    work_start_date = models.DateField("Data początku",null=True)
    work_stop_date = models.DateField("Data początku",null=True)
    work_date = models.DateField("Data generacji", default=timezone.now , null=True)
    class Meta:
        verbose_name_plural = "Harmonogram"

class Term_day(models.Model):
    DAY = (
        ('0', ('Poniedziałek')),
        ('1', ('Wtorek')),
        ('2', ('Środa')),
        ('3', ('Czwartek')),
        ('4', ('Piątek')),
        ('5', ('Sobota')),
        ('6', ('Niedziela')),
    )
    work_place = models.ForeignKey(Unit, on_delete=models.PROTECT, null=True, verbose_name="Jednostka")
    work_person = models.ForeignKey(Personal_med, on_delete=models.PROTECT, null=True, verbose_name="Osoba personelu")
    work_date = models.DateField("Data", null=True)
    work_time = models.TimeField(auto_now=False, auto_now_add=False, verbose_name="Godzina wizyty")
    work_day = models.CharField("Dzień tygodnia", max_length=100, null=True, choices=DAY)
    work_type = models.CharField("Typ terminarza", max_length=100, null=True)


    def __str__(self):

        text_date = self.work_date.strftime("%m/%d/%Y")
        text_time = self.work_time.strftime("%H:%M:%S")
        return (text_date +' '+ text_time)

    class Meta:
        verbose_name_plural = "Terminarz"
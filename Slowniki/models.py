from django.db import models

# Create your models here.
class ICD9(models.Model):
    kod = models.CharField("Kod", max_length=10, null=True, unique=True, blank=False)
    nazwa = models.CharField("Nazwa", max_length=200, null=True, unique=True, blank=False)
    def __str__(self):
        return self.kod +" "+ self.nazwa
    class Meta:

        verbose_name_plural = "Słownik ICD9"

class ICD10(models.Model):
    kod = models.CharField("Kod", max_length=10, null=True, unique=True, blank=False)
    nazwa = models.CharField("Nazwa", max_length=200, null=True, unique=True, blank=False)
    def __str__(self):
        return self.kod +" "+ self.nazwa
    class Meta:

        verbose_name_plural = "Słownik ICD10"
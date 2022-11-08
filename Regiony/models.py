from django.db import models

# Create your models here.



class Regional(models.Model):
    name_reg = models.CharField("Nazwa",max_length=50)
    def __str__(self):

     return self.name_reg

    class Meta:

        verbose_name_plural = "Województwa"


# ------------------------------------------------
# class Powiat(models.Model):
#     id_reg = models.ForeignKey(Regional, on_delete=models.PROTECT, null=True)
#     name = models.CharField("Nazwa", max_length=50)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name_plural = "Powiaty"
# ------------------------------------------------
class City(models.Model):
    id_reg = models.ForeignKey(Regional, on_delete=models.PROTECT, null=True)

    name_city = models.CharField("Nazwa",max_length=50)

    def __str__(self):
        return self.name_city

    class Meta:
        verbose_name_plural = "Miasta"
# ------------------------------------------------


from django.contrib import *
from .models import *
from django.contrib.auth.models import *
from import_export import resources
from import_export.admin import  ImportExportModelAdmin
# Register your models here.
class AdminPersonel(resources.ModelResource):
    class Meta:
        model = Personal
class AdminMed(resources.ModelResource):
    class Meta:
        model = Personal_med

class PersonelHead(ImportExportModelAdmin):
    resource_class = AdminPersonel
    list_display =['id','last_name', 'first_name', 'iduser', 'pesel', 'IDname', 'IDnumber', 'date_brith', 'phone', 'regional_woj', 'regional_city', 'post' , 'str_name', 'str_number', 'str_number_one', 'doc', 'Register_date', 'check']
class PersonelMEDHead(ImportExportModelAdmin):
    resource_class = AdminMed
    list_display =['id','last_name', 'first_name', 'iduser', 'pesel', 'date_brith', 'npwz' , 'phone', 'regional_woj', 'regional_city', 'str_name', 'str_number', 'str_number_one', ]


admin.site.register(Personal_med, PersonelMEDHead),
admin.site.register(Personal, PersonelHead),

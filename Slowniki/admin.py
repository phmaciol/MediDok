from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import  ImportExportModelAdmin
# Register your models here.

class ImportICD9(resources.ModelResource):
        class Meta:
                model=ICD9
class ImportICD10(resources.ModelResource):
        class Meta:
                model=ICD10


class ICD9IMP(ImportExportModelAdmin):
        resource_class = ImportICD9
        list_display = ['kod', 'nazwa']
class ICD10IMP(ImportExportModelAdmin):
        resource_class = ImportICD10
        list_display = ['kod', 'nazwa']

admin.site.register(ICD9, ICD9IMP),
admin.site.register(ICD10, ICD10IMP),

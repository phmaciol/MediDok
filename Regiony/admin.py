from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import  ImportExportModelAdmin
# Register your models here.
class Reg_ImportExport(resources.ModelResource):
    class Meta:
        model = Regional

class City_ImportExport(resources.ModelResource):
    class Meta:
        model = City



class Regional_import(ImportExportModelAdmin):
    resource_class = Reg_ImportExport
    list_display = ['id', 'name_reg']


class City_import(ImportExportModelAdmin):
    resource_class = City_ImportExport
    list_display = ['id', 'id_reg', 'name_city']


admin.site.register(Regional, Regional_import),
admin.site.register(City, City_import),

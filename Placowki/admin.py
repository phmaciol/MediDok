from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import  ImportExportModelAdmin
# Register your models here.
class AdminNFZ(resources.ModelResource):
    class Meta:
        model = NFZ
class AdminOrganization(resources.ModelResource):
    class Meta:
        model = Organization
class AdminStruct(resources.ModelResource):
    class Meta:
        model = Struct_Organization
class AdminUnit(resources.ModelResource):
    class Meta:
        model = Unit
class AdminDoctor(resources.ModelResource):
    class Meta:
        model = doctor
# <------------------------------------------------------------>
class Admin_Site_NFZ(ImportExportModelAdmin):
    resource_class = AdminNFZ
    list_display = ['id', 'name', 'regional']

class Admin_Site_Organization(ImportExportModelAdmin):
    resource_class = AdminNFZ
    list_display = ['id', 'name', 'nip', 'regon', 'krs', 'number_resort', 'number_swiat', 'oddz_nfz', 'logo']


class Admin_Site_Struct(ImportExportModelAdmin):
    resource_class = AdminNFZ
    list_display = ['id', 'name', 'organization', 'city', 'adress1', 'adress2', 'adress3', 'phone', 'mail', 'logo', 'type_place']


class Admin_Site_Unit(ImportExportModelAdmin):
    resource_class = AdminNFZ
    list_display = ['id', 'name', 'organization', ]

class Admin_Site_Doctor(ImportExportModelAdmin):
    resource_class = AdminDoctor
    list_display = ['id', 'first_name', 'last_name', 'name', 'unit']
# <------------------------------------------------------------>
admin.site.register(NFZ, Admin_Site_NFZ),
admin.site.register(Organization, Admin_Site_Organization),
admin.site.register(Struct_Organization, Admin_Site_Struct ),
admin.site.register(Unit, Admin_Site_Unit),
admin.site.register(doctor, Admin_Site_Doctor),
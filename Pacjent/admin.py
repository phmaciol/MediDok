from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import  ImportExportModelAdmin
# Register your models here.
class DocResource(resources.ModelResource):
        class Meta:
                model=Document
class VisitResource(resources.ModelResource):
        class Meta:
                model=Visit
class EskierResource(resources.ModelResource):
        class Meta:
                model=e_system_SKIEROWANIA
class ErecResource(resources.ModelResource):
        class Meta:
                model=e_system_RECEPTY
class DocHead(ImportExportModelAdmin):
        resource_class = DocResource
        list_display = ['name', 'author_user', 'author_person', 'doc']

class VisitHead(ImportExportModelAdmin):
        resource_class = VisitResource
        list_display = ['id', 'patient_user', 'patient_person', 'organization', 'struct', 'unity', 'confirmation']
class SKIe_sys(ImportExportModelAdmin):
        resource_class = EskierResource
        list_display = ['id', 'key_e', 'idvisit', 'idpac', 'iddoc']
class RECe_sys(ImportExportModelAdmin):
        resource_class = ErecResource
        list_display = ['id', 'key_e', 'idvisit', 'idpac', 'iddoc']
class FormHead(ImportExportModelAdmin):
        list_display = ['name']
class FormUserHead(ImportExportModelAdmin):
        list_display = ['name', 'patient_person', 'type_forms', 'status', 'remarks_user', 'remarks_person', 'name_unit', 'publish_date', 'file' ]
admin.site.register(Document, DocHead),
admin.site.register(Visit, VisitHead),
admin.site.register(e_system_SKIEROWANIA, SKIe_sys),
admin.site.register(e_system_RECEPTY, RECe_sys),
admin.site.register(Form_all, FormHead),
admin.site.register(Form_user, FormUserHead),
admin.site.register(dekl),
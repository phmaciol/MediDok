from django.contrib import *
from .models import *
from django.contrib.auth.models import *
from import_export import resources
from import_export.admin import  ImportExportModelAdmin
# Register your models here.
class AdminHarm(resources.ModelResource):
    class Meta:
        model = Term
class AdminTerm(resources.ModelResource):
    class Meta:
        model = Term_day
# Register your models here.
class HarmoAdmin(ImportExportModelAdmin):
    resource_class = AdminHarm
    list_display =['work_place', 'work_person', 'work_type', 'work_start', 'work_stop', 'work_day', 'work_time' ]
class TermAdmin(ImportExportModelAdmin):
    resource_class = AdminHarm
    list_display =['work_place', 'work_person', 'work_date', 'work_time', 'work_day', 'work_type']

admin.site.register(Term, HarmoAdmin),
admin.site.register(Term_day, TermAdmin),
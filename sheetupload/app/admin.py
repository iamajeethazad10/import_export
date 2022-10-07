from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from .models import Person


@admin.register(Person)
class PersonAdmin(ImportExportActionModelAdmin):
    list_display = ('name', 'email', 'location')

from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.
class ConversionScoreResource(resources.ModelResource):
    class Meta:
        model = ConversionScore

class ConversionScoreAdmin(ImportExportModelAdmin):
    resource_class = ConversionScoreResource

admin.site.register(ConversionScore, ConversionScoreAdmin)

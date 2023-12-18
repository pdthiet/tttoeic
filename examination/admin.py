from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.
admin.site.register(Audio)

class ImageResource(resources.ModelResource):
    class Meta:
        model = Image

class ImageAdmin(ImportExportModelAdmin):
    resource_class = ImageResource

admin.site.register(Image, ImageAdmin)

class ExaminationResource(resources.ModelResource):
    class Meta:
        model = Examination

class ExamiantionAdmin(ImportExportModelAdmin):
    resource_class = ExaminationResource

admin.site.register(Examination, ExamiantionAdmin)
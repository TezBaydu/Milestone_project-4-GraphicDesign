from django.contrib import admin
from .models import Project, Company

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'company',
        'image',
    )

    ordering = ('sku',)


class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
        'description',
    )

    ordering = ('name',)


admin.site.register(Project, ProjectAdmin)
admin.site.register(Company, CompanyAdmin)

from django.contrib import admin
from users.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
from import_export.admin import ImportExportMixin
from core.models import OrgUnits, DataElement, Indicator, DataValueSet, Program

class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name',)}),
        (
            _('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        (_('Important dates'), {'fields': ('last_login',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )

class OrgUnitsAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = [
        'id',
        'us_name',
        'province_name',
        'district_name'
    ]

class DataElementsAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = [
        'id',
        'name'
    ]

class IndicatorAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'numerator_names',
        'numerator'
    ]

class DataValueSetAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = [
        'data_element',
        'period',
        'orgunit',
        'categoryOptionCombo',
        'attributeOptionCombo',
        'value'
    ]

class ProgramAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = [
        'id',
        'name'
    ]

admin.site.register(User, UserAdmin)
admin.site.register(OrgUnits, OrgUnitsAdmin)
admin.site.register(DataElement, DataElementsAdmin) 
admin.site.register(Indicator, IndicatorAdmin)
admin.site.register(DataValueSet, DataValueSetAdmin)
admin.site.register(Program, ProgramAdmin)
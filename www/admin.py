from django.contrib import admin
from django.utils.html import format_html

from . import models

class SportSiteAdmin(admin.ModelAdmin):
    list_display = ('appellation', 'departement', 'commune', 'code_postal', 'site_olympique', 'preview_image')
    search_fields = ('appellation', 'commune', 'adresse_com')
    list_filter = ('departement', 'typologie', 'denomination')

    def preview_image(self, obj):
        if obj.url_image:
            return format_html('<img src="{}" width="100" height="100" />', obj.url_image)
        return "No Image"

admin.site.register(models.sportSite, SportSiteAdmin)
admin.site.register(models.Typo)
admin.site.register(models.Denomination)
admin.site.register(models.DateReference)
admin.site.register(models.site)

    

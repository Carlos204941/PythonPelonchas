from django.contrib import admin

# Register your models here.
from .models import Plat


class PlatAdmin(admin.ModelAdmin):
    list_display = ('nom', 'categorie', 'ingredients', 'vegetarienne', 'prix')
    search_fields = ['nom', 'categorie']


admin.site.register(Plat, PlatAdmin)

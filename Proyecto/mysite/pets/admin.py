from django.contrib import admin

from .models import Pets

class PetsAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'history', 'image')
    list_display = ('__str__', 'slug', 'created_at')


admin.site.register(Pets, PetsAdmin)

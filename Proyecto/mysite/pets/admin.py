from django.contrib import admin

from .models import Pets


class PetsAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'history', 'image', 'image2', 'image3', 'image4', 'state')
    list_display = ('__str__', 'slug', 'created_at', 'state')
    list_filter = [ 'created_at', 'state' ]

admin.site.register(Pets, PetsAdmin)

from django.contrib import admin
from .models import Adoption

# Register your models here.

class AdoptionAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created_at')


admin.site.register(Adoption, AdoptionAdmin)
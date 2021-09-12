from django.contrib import admin
from .models import Pet
from .models import Document
from .models import Donation
from .models import Adopcion
from .models import User
from .models import Solicitud
# Register your models here.

#admin.site.register(Solicitud)
# admin.site.register(User)
# admin.site.register(Adopcion)
admin.site.register(Donation)
admin.site.register(Document)
# admin.site.register(Pet)


@admin.register(User) 
class UserAdmin(admin.ModelAdmin):
    list_display = ["name", "no_document", "email"]
    # list_display_links = ["name"]
    # list_editable = ["name"]
    search_fields = ["name"]
    list_filter = ["no_document"]
    list_per_page = 10

@admin.register(Adopcion) 
class AdopcionAdmin(admin.ModelAdmin):
    list_display = ["name", "pet_age", "breed"]
    # list_display_links = ["name"]
    # list_editable = ["name"]
    search_fields = ["name"]
    list_filter = ["breed"]
    list_per_page = 10

@admin.register(Solicitud) 
class SolicitudAdmin(admin.ModelAdmin):
    list_display = ["name", "phone", "email", "nuDocument", "location", "mascota_id"]
    # list_display_links = ["name"]
    # list_editable = ["name"]
    search_fields = ["name"]
    list_filter = ["name"]
    list_per_page = 10

@admin.register(Pet) 
class PetAdmin(admin.ModelAdmin):
    list_display = ["name", "pet_age", "breed", "description"]
    # list_display_links = ["name"]
    # list_editable = ["name"]
    search_fields = ["name"]
    list_filter = ["breed"]
    list_per_page = 10
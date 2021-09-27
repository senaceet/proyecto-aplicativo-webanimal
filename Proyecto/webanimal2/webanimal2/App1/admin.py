from django.contrib import admin
from .models import contacts
from .models import Donation
from .models import Location
from .models import Neighborhood
from .models import Document
from .models import dog_breed
from .models import cat_breed
from .models import questionnaire
from .models import breed
from .models import mascot
from .models import request_adoption
from .models import Adoption
from .models import user_register
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
from django.contrib import admin
from .models import Contacts, cat, dog
from .models import Location
from .models import Neighborhood
from .models import Document
from .models import Questionnaire
from .models import Breed
from .models import Mascot
from .models import User_register
from .models import Request_adoption
from .models import Adoption
from .models import Donation

# Register your models here.

admin.site.register(Contacts)
admin.site.register(Location)
admin.site.register(Neighborhood)
admin.site.register(Document)
admin.site.register(dog)
admin.site.register(cat)
admin.site.register(Questionnaire)
admin.site.register(Breed)
admin.site.register(Mascot)
admin.site.register(User_register)
admin.site.register(Request_adoption)
admin.site.register(Adoption)
admin.site.register(Donation)


# @admin.register(Contacts) 
# class ContactsAdmin(admin.ModelAdmin):
#     list_display = ["name", "email", "phone", "affair", "message"]
#     # list_display_links = ["name"]
#     # list_editable = ["name"]
#     search_fields = ["name"]
#     list_filter = ["name"]
#     list_per_page = 10

# @admin.register(Location) 
# class LocationAdmin(admin.ModelAdmin):
#     list_display = ["description"]
#     # list_display_links = ["name"]
#     # list_editable = ["name"]
#     search_fields = ["name"]
#     list_filter = ["description"]
#     list_per_page = 10

# @admin.register(Neighborhood) 
# class NeighborhoodAdmin(admin.ModelAdmin):
#     list_display = ["description", "localidad"]
#     # list_display_links = ["name"]
#     # list_editable = ["name"]
#     search_fields = ["name"]
#     list_filter = ["localidad"]
#     list_per_page = 10

# @admin.register(Document) 
# class DocumentAdmin(admin.ModelAdmin):
#     list_display = ["description"]
#     # list_display_links = ["name"]
#     # list_editable = ["name"]
#     search_fields = ["name"]
#     list_filter = ["description"]
#     list_per_page = 10

# @admin.register(Dog_breed) 
# class Dog_breedAdmin(admin.ModelAdmin):
#     list_display = ["description"]
#     # list_display_links = ["name"]
#     # list_editable = ["name"]
#     search_fields = ["name"]
#     list_filter = ["description"]
#     list_per_page = 10

# @admin.register(Cat_breed) 
# class Cat_breedAdmin(admin.ModelAdmin):
#     list_display = ["description"]
#     # list_display_links = ["name"]
#     # list_editable = ["name"]
#     search_fields = ["name"]
#     list_filter = ["description"]
#     list_per_page = 10

# @admin.register(Questionnaire) 
# class QuestionnaireAdmin(admin.ModelAdmin):
#     list_display = ["question1", "question2", "question3", "question4", "question5"]
#     # list_display_links = ["name"]
#     # list_editable = ["name"]
#     search_fields = ["name"]
#     list_filter = ["question1"]
#     list_per_page = 10

# @admin.register(Breed) 
# class BreedAdmin(admin.ModelAdmin):
#     list_display = ["description", "raza_perros", "raza_gatos"]
#     # list_display_links = ["name"]
#     # list_editable = ["name"]
#     search_fields = ["name"]
#     list_filter = ["raza_perros"]
#     list_per_page = 10

# @admin.register(Mascot) 
# class MascotAdmin(admin.ModelAdmin):
#     list_display = ["name", "pet_age", "description"]
#     # list_display_links = ["name"]
#     # list_editable = ["name"]
#     search_fields = ["name"]
#     list_filter = ["pet_age"]
#     list_per_page = 10

# @admin.register(User_register) 
# class User_registerAdmin(admin.ModelAdmin):
#     list_display = ["name", "document", "Email", "password", "telephone", "birth_date", "direction"]
#     # list_display_links = ["name"]
#     # list_editable = ["name"]
#     search_fields = ["name"]
#     list_filter = ["document"]
#     list_per_page = 10

# @admin.register(Request_adoption) 
# class Request_adoptionAdmin(admin.ModelAdmin):
#     list_display = ["message"]
#     # list_display_links = ["name"]
#     # list_editable = ["name"]
#     search_fields = ["name"]
#     list_filter = ["message"]
#     list_per_page = 10

# @admin.register(Adoption) 
# class AdoptionAdmin(admin.ModelAdmin):
#     list_display = ["description"]
#     # list_display_links = ["name"]
#     # list_editable = ["name"]
#     search_fields = ["name"]
#     list_filter = ["description"]
#     list_per_page = 10

# @admin.register(Donation) 
# class DonationAdmin(admin.ModelAdmin):
#     list_display = ["description"]
#     # list_display_links = ["name"]
#     # list_editable = ["name"]
#     search_fields = ["name"]
#     list_filter = ["description"]
#     list_per_page = 10

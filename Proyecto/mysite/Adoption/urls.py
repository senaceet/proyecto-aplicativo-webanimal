from django.urls import path
from . import views


urlpatterns = [
    path('', views.frmAdoption, name='Adoption')
]
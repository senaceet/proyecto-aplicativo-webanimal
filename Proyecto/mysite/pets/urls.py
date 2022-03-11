from django.urls import path

from . import views

app_name = 'pets'

urlpatterns = [
    path('search', views.PetsSearchListView.as_view(), name='search'),
    path('<slug:slug>', views.PetsDetailView.as_view(), name='pets'),
]
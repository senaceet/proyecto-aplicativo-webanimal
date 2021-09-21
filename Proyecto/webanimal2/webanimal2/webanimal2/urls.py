"""webanimal2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LoginView,logout_then_login
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('donaciones/', views.Donaciones, name='Donaciones'),
    path('contactosWebanimal/', views.Contactos, name='ContactosWebanimal'),
    path('frmadopcion/', views.frmadopcion, name='frmadopcion'),
    path('register/', views.register, name='register'),
    path('acceder/', views.acceder, name='acceder'),
    path('nosotros/', views.Nosotros, name='Nosotros'),
    path('pagina_inicio/', views.Pagina_Inicio, name='Pagina_Inicio'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]

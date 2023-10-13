
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Assult', views.unit1, name='ASSAULT'),
    path('HeavyAssult', views.unit2, name='HEAVY ASSAULT'),
    # path('FireAssult', views.unit2, name='Fire Assult'),
    # path('Fortress', views.unit3, name='Fortress'),
    # path('Hammer', views.unit4, name='Hammer'),
    # path('Zeus', views.unit5, name='Zeus'),
    # path('Coyote', views.unit6, name='Coyote'),
    # path('Armadillo', views.unit7, name='Armadillo'),
    # path('Jaguar', views.unit8, name='Jaguar'),
    # path('Rifleman', views.unit9, name='Rifleman'),
    # path('Grenadier', views.unit10, name='Grenadier'),
    # path('Sniper', views.unit11, name='Sniper')
]

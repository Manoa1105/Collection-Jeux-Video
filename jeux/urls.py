from django.urls import path
from . import views
urlpatterns=[
    path('ajouter/', views.ajouter_jeu, name='ajouter_jeu'),
    path('listing', views.list_jeux,name='list_jeux'),
    path('modifier/<int:id>/', views.modifier_jeu, name='modifier_jeu'),
    path('supprimer/<int:id>/', views.supprimer_jeu, name='supprimer_jeu'),
    path('jeux/confirmation/<int:pk>/', views.confirmer_suppression, name='confirmer_suppression'),
]
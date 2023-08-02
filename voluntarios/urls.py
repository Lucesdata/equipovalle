from django.urls import path
from . import views

urlpatterns = [
    path('voluntarios/', views.formulario_voluntario, name='formulario_voluntario'),
    path('gracias/', views.agradecimiento, name='gracias'),
    path('voluntarios_totales/', views.voluntarios_totales, name='voluntarios_totales'),
]

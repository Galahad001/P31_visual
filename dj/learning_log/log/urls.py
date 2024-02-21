from django.urls import path
from . import views

app_name = 'lod'
urlpatterns = [
    path('', views.index, name='index')
]

from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('place',views.place, name='place'),
    path('contact',views.contact, name='contact'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('',views.homi),
    path('log',views.log),
    path('admhom',views.admhom),
    path('addc',views.addcourse),
]

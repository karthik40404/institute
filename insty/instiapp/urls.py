from django.urls import path
from . import views

urlpatterns = [
    path('',views.homi,name='home'),
    path('viewcourse/<cid>',views.viewcourse,name='viewcourse'),
    path('contact',views.contact),
    path('placement',views.placements),
    path('smessage',views.sendm),
]

from django.urls import path

from . import views

urlpatterns = [
        path('',views.homepage, name='homepage'),
        path('map/',views.map, name='map'),
        path('sightings/',views.sighting, name='sighting'),
        path('sightings/add/',views.add_squirrel, name='add_squirrel'),
        path('sightings/<str:Unique_Squirrel_Id>/',views.update, name='update'),
        path('sightings/stats/',views.stats, name='stats'),
        ]

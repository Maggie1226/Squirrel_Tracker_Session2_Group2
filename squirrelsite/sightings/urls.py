from django.urls import path
from . import views

urlpatterns=[
        path('',views.all_squirrels),
        path('<str:squirrel_id>/',views.edit_squirrel),
        path('add/',views.add),
        path('stats/',views.stats),
        ]

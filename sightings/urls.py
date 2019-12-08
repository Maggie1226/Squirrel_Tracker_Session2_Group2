from django.urls import path,re_path
from . import views

urlpatterns=[
        path('',views.all_squirrels),
        re_path(r'(\d.*)/',views.edit_squirrel),
        path('add/',views.add),
        path('stats/',views.stats),
        ]

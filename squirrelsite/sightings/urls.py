from django.urls import path,re_path
from . import views

urlpatterns=[
        path('',views.all_squirrels),
        re_path(r'(\d{2}[a-zA-Z].[a-zA-Z]{2}.\d{4}.\d{2})/',views.edit_squirrel),
        path('add/',views.add),
        path('stats/',views.stats),
        ]

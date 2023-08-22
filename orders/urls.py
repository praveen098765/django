from django.urls import path
from . import views

urlpatterns = [
    path('table/', views.index3, name='index3'),
     path('table2/', views.index2, name='index2'),
]

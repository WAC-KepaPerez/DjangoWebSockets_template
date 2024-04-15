from django.urls import path
from . import views



urlpatterns=[
    path('', views.HelloView.as_view(), name='hello'),
    path('example', views.Example.as_view(), name='hello'),
]

from django.urls import path
from . import views


urlpatterns=[
    path('',views.index),
    path('mac',views.mac),
    path('login',views.login)
    
]

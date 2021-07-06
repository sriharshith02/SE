from django.urls import path
from projapp import views
urlpatterns=[
    path('',views.index,name="index"),
    path('Registration',views.Registration,name="Registration"),
    path('dash',views.dash,name="dash"),
]

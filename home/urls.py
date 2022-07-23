from django.urls import include, path
from .views import *

urlpatterns = [
    path('',home, name="home"),
    path('register/<slug>',registration, name="register"),
    path('api/form/stay_in_touch', sitform, name="stay in touch"),
    path('api/form/subscribe',subscribe, name="subscribe to newsletter"),
    path('api/form/register_startup',startup_register,name="register your team")
]
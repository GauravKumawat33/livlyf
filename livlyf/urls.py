from django.urls import path
from . import views

urlpatterns = [
    path('about/',views.About,name='about'),
    path('',views.Home,name='home'),
    path('contact/',views.Contact,name='contact'),


]

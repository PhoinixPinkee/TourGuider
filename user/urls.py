from django.urls import path
from . import views
urlpatterns=[
    path('',views.home),
    path('home/', views.home),
    path('about/', views.about),
    path('contactus/', views.contactus),
    path('guiderdetails/', views.guiderdetails),
    path('newplaces/', views.newplaces),
    path('signin/', views.signin),
    path('gallery/',views.imagegallery),
    path('video/',views.videogallery),
    path('viewdetails/',views.viewdetails),

]
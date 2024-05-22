from django.urls import path
from.import views


urlpatterns = [
    #path('', views.home, name='home'),
    path('',views.home, name='home_blog'),
    #path('about/', views.hello, name='hi'),
    path('myhome/', views.myhome, name='myhome2'),
    path('about/', views.about, name='about_blog'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('dishdetail/', views.dishdetail, name='dishdetail'),
    path('gallery/', views.gallery, name='gallery'),
    path('chef/', views.chef, name='chef'),
    path('booktable/', views.booktable, name='booktable'),
    path('feedback/', views.feedback, name='feedback'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('booking-success/', views.booking_success, name='booking_success'),
    path('owner/', views.owner, name='owner'),
]
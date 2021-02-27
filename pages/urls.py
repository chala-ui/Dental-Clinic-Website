from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('blog-details/', views.blog_details, name='blog-details'),
    path('blog/', views.blog, name='blog'),
    path('pricing/', views.pricing, name='pricing'),
    path('services/', views.services, name='services'),
    path('appointment/', views.appointment, name='appointment'),
]   
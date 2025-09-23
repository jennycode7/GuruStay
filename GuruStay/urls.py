from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='Homepage'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('dashboard/<int:pk>/book', views.BookingCreateView.as_view(), name='book_property'),
    path('property_form/', views.PropertyCreateView.as_view(), name='property_form'),
    path('host/', views.become_host, name='become_host')
]
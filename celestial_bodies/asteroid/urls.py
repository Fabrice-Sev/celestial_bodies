from django.urls import path

from . import views

urlpatterns = [
    path('', views.asteroid_with_dates, name='asteroids_with_dates'),
    path('details/<int:asteroid_id>', views.asteroid_details, name='asteroid_details')
]
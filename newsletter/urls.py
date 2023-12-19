from django.urls import path
from .views import newsletter, newsletter_success
from . import views

urlpatterns = [
    path('newsletter/', views.newsletter, name='newsletter'),
    path('newsletter_success/', views.newsletter_success,
         name='newsletter_success'),
]

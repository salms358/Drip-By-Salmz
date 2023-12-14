from django.urls import path
from .import views

urlpatterns = [
    path('', views.show_likes, name='likes'),
    path('add_likes/<int:product_id>/',
         views.add_or_remove_likes,
         name='add_likes'),
]
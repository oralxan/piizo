from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_list, name='menu_list'),
    path('menu/<int:id>/', views.menu_detail, name='menu_detail'),
    path('news/', views.news_list, name='news_list'),
    path('news/<int:id>/', views.news_detail, name='news_detail'),  # Update this line
    path('recipes/', views.recipe_list, name='recipe_list'),
    path('contact/', views.contact, name='contact'),
]

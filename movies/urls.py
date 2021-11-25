from django.urls import path, include
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    path('<int:movie_pk>/likes/', views.likes, name='likes'),
    path('recommended/', views.recommended, name='recommended'),
    path('random_movie/', views.random_movie, name='random_movie'),
    path('christmas/', views.christmas, name='christmas'),
    path('search/', views.search, name='search'),
]
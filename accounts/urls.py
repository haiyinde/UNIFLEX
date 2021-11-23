from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('follow/<int:user_pk>/', views.follow, name='follow'),
    path('profile/<username>/', views.profile, name='profile'),
    # path('test/<username>/', views.test, name='test'),    
]
from django.urls import path, include
from . import views

app_name = 'community'

urlpatterns = [
    # review
    path('',views.index, name='index'),
    path('create/',views.create, name='create'),
    path('<int:review_pk>/',views.detail, name='detail'),
    path('update/<int:review_pk>/',views.update, name='update'),
    path('delete/<int:review_pk>/',views.delete, name='delete'),
    # review like
    path('<int:review_pk>/likes/',views.likes, name='likes'),
    # comment
    path('<int:review_pk>/comment/',views.comment,name='comment'),
    path('<int:review_pk>/comment/<int:comment_pk>/delete/',views.comment_delete, name='comment_delete'),
    path('<int:review_pk>/comment/<int:comment_pk>/update/',views.comment_update, name='comment_update'),
]

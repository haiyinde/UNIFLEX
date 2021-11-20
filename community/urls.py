from django.urls import path, include
from . import views

app_name = 'community'

urlpatterns = [
    # review
    path('',views.index, name='index'),
    path('create/',views.create, name='create'),
    path('delete/<int:pk>/',views.delete, name='delete'),
    path('update/<int:pk>/',views.update, name='update'),
    # comment
    path('<int:review_pk>/',views.comment,name='comment'),
    path('<int:review_pk>/comment/<int:comment_pk>',views.comment_del,name='comment'),
]

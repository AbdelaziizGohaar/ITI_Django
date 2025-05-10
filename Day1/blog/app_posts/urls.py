from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.all_posts) ,
    path('<str:post_title>/',views.post_details , name = 'post_details'),
]

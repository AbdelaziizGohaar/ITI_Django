from django.urls import path,include
from . import views

urlpatterns = [
    path('all', views.all_posts) ,
    # path('<str:post_title>/',views.post_details , name = 'post_details'),
    #-------------------------------------------------------------------------
    path('', views.home, name='home'),
    path('<int:pk>/', views.post_detail, name='post_detail'),  # Uses post ID
    path('author/<int:pk>/', views.author_profile, name='author_profile'),
]

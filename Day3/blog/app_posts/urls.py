from django.urls import path,include
from . import views
from .views import (PostListCreate, PostRetrieveUpdateDestroy, AuthorListCreate, AuthorRetrieveUpdateDestroy)


urlpatterns = [
    path('all', views.all_posts) ,
    # path('<str:post_title>/',views.post_details , name = 'post_details'),
    #-------------------------------------------------------------------------
    path('posts/', views.home, name='home'),
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),  # Uses post ID
    path('author/<int:pk>/', views.author_profile, name='author_profile'),

    #============================== API =============================
    path('api/posts/', PostListCreate.as_view()),
    path('api/posts/<int:pk>/', PostRetrieveUpdateDestroy.as_view()),
    
    # Author endpoints
    path('api/authors/', AuthorListCreate.as_view()),
    path('api/authors/<int:pk>/', AuthorRetrieveUpdateDestroy.as_view()),
]

from django.shortcuts import render, get_object_or_404
from .models import Post, Author
from django.http import HttpResponse

#----------------------------
from rest_framework import generics
from .models import Post, Author
from .serializers import PostSerializer, AuthorSerializer


posts = [
]


# Create your views here.


#=========== all posts Methods ==========================
def all_posts(request):
    context = {
        'posts': posts
    }
    return render(request , 'posts/all_posts.html', context = context)


#=========== home Methods ===============
def home(request):
    posts = Post.objects.all().order_by('-date_posted')  # araga3 el Newest awel
    return render(request, 'posts/home.html', {'posts': posts})


#=========== PostDetails Methods ===============
def post_detail(request, pk):  # Using PK instead of title for reliability
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/post_details.html', {'post': post})


#=========== Author Methods ===============
def author_profile(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render(request, 'posts/author_profile.html', {'author': author})

#=========================================  API  =================================================================


# Post Views
class PostListCreate(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# Author Views
class AuthorListCreate(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
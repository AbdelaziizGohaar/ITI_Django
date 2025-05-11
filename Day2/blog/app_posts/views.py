from django.shortcuts import render, get_object_or_404
from .models import Post, Author
from django.http import HttpResponse

posts = [
]


# Create your views here.

# #=========== Index Methods ===============
# def index(request):
#     return HttpResponse("hello index")


#=========== all posts Methods ==========================
def all_posts(request):
    context = {
        'posts': posts
    }
    return render(request , 'posts/all_posts.html', context = context)


# #=========== Post Details  Methods ==========================
# def post_details(request, post_title):
#     for post in posts:
#         if post['title'].lower() == post_title.lower():
#             context = {
#                 'post': post
#             }
#             return render(request , 'posts/post_details.html', context = context)
        


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




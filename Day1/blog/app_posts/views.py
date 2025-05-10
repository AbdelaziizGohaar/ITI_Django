from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'id': 1,
        'title': 'The Power of Morning Routines',
        'content': 'Establishing a consistent morning routine can boost your productivity, mindset, and energy levels throughout the day.',
         'image': 'images/post1.jpeg',
        'created_at': '2025-04-01',
    },
    {
        'id': 2,
        'title': 'Top 10 Travel Destinations for 2025',
        'content': 'From the beaches of Bali to the mountains of Switzerland, explore the best places to travel this year.',
         'image': 'images/post2.jpeg',
        'created_at': '2025-04-03',
    },
    {
        'id': 3,
        'title': 'Simple Recipes for Busy Weeknights',
        'content': 'These 30-minute meals are perfect for anyone juggling a busy schedule but still wants to eat well.',
         'image': 'images/post3.jpeg',
        'created_at': '2025-04-05',
    },
    {
        'id': 4,
        'title': 'How to Start Investing with Little Money',
        'content': 'Learn how to enter the world of investing even if you’re starting with $100 or less.',
         'image': 'images/post4.jpeg',
        'created_at': '2025-04-07',
    },
    {
        'id': 5,
        'title': 'The Benefits of Daily Meditation',
        'content': 'Meditation can reduce stress, improve focus, and enhance overall well-being. Here’s how to get started.',
         'image': 'images/post6.jpeg',
        'created_at': '2025-04-09',
    },
    {
        'id': 6,
        'title': 'Must-Read Books for Personal Growth',
        'content': 'These inspiring books can help you develop better habits, mindset, and life skills.',
         'image': 'images/post5.jpeg',
        'created_at': '2025-04-11',
    },
    {
        'id': 7,
        'title': 'A Beginner’s Guide to Gardening',
        'content': 'Want to grow your own food or flowers? Start with these beginner tips and tools.',
         'image': 'images/post1.jpeg',
        'created_at': '2025-04-13',
    },
    {
        'id': 8,
        'title': 'Freelancing: How to Find Your First Client',
        'content': 'Breaking into freelancing? Here’s how to pitch your services and land your first paying gig.',
         'image': 'images/post5.jpeg',
        'created_at': '2025-04-15',
    },
    {
        'id': 9,
        'title': 'Creating a Minimalist Lifestyle',
        'content': 'Declutter your home and mind by embracing minimalism — fewer things, more meaning.',
         'image': 'images/post2.jpeg',
        'created_at': '2025-04-17',
    },
]


# Create your views here.
def index(request):
    return HttpResponse("hello index")


#=========== all posts Methods ==========================
def all_posts(request):
    context = {
        'posts': posts
    }
    return render(request , 'posts/all_posts.html', context = context)


#=========== Post Details  Methods ==========================
def post_details(request, post_title):
    for post in posts:
        if post['title'].lower() == post_title.lower():
            context = {
                'post': post
            }
            return render(request , 'posts/post_details.html', context = context)
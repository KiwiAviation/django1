from django.shortcuts import render

posts = [
    {
        'author': 'KiwiAviation',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'July 13, 2020'
    },
    {
        'author': 'John Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'July 14, 2020'
    }
]

def home(request):
    context={
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

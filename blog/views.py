from django.shortcuts import get_object_or_404, render
from django.http import Http404
from datetime import date
from blog.models import Post

# Create your views here

def get_date(post):
    #print(post['date'])
    return post['date']

def index(request):
    sorted_posts = Post.objects.all().order_by('-date')[:3] # This whole expression is converted into a SQL-command => better performance. Thanks Django :)
    latest_posts = sorted_posts[0:3]
    print(latest_posts)
    return render(request, 'blog/index.html', {'posts': latest_posts})


def all_posts(request):
    all_posts = Post.objects.all().order_by('date')
    return render(request, 'blog/all_posts.html', {'all_posts': all_posts})


def single_post(request, slug):
    identified_post = get_object_or_404(Post, slug=slug)
    print(identified_post)
    return render(request, 'blog/post-detail.html', {"post": identified_post,
                                                     "post_tags": identified_post.tags.all()})



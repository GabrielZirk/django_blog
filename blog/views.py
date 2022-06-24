from django.shortcuts import render
from django.http import Http404
from datetime import date

# Create your views here.

posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Gabi",
        "date": date(2021, 7, 21),
        "title": "Doggo",
        "excerpt": "I love dogs",
        "content": """Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor 
        invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo 
        duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. 
        Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut 
        labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et 
        ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."""
    },
    {
        "slug": "catto",
        "image": "woods.jpg",
        "author": "Gabi",
        "date": date(2021, 6, 21),
        "title": "Catto",
        "excerpt": "I love cats",
        "content": """AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"""
    },
    {
        "slug": "animalo",
        "image": "coding.jpg",
        "author": "Gabi",
        "date": date(2021, 5, 21),
        "title": "Animalo",
        "excerpt": "I love all animals",
        "content": """BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
        BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
        """
    },
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Gabi",
        "date": date(2021, 4, 21),
        "title": "Mountain Hiking",
        "excerpt": "There is nothing like the views you get when hiking in the mountians",
        "content": """Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor 
        invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo 
        duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. 
        Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut 
        labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et 
        ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."""
    }
]

def get_date(post):
    #print(post['date'])
    return post['date']

def index(request):
    sorted_posts = sorted(posts, key=lambda x: x['date'], reverse=True)
    latest_posts = sorted_posts[0:3]
    print(latest_posts)
    return render(request, 'blog/index.html', {'posts': latest_posts})


def all_posts(request):
    return render(request, 'blog/all_posts.html', {'all_posts': posts})


def single_post(request, slug):
    identified_post = next(post for post in posts if post['slug'] == slug)
    return render(request, 'blog/post-detail.html', {"post": identified_post})



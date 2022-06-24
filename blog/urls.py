from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('posts', views.all_posts, name='all_posts'),
    path('posts/<slug:slug>', views.single_post, name='single_post')

    # The slug-transformer: Slug is a newspaper term. A slug is a short label for something,
    # containing only letters, numbers, underscores or hyphens. They’re
    # generally used in URLs.

]

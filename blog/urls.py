from django_distill import distill_path
from django.core.paginator import Paginator
from .views import IndexView, PostView, TagView, ContactView
from .models import Post, Tag


def get_index():
    return None

def get_contact():
    return None

def get_paginated_index():
    posts = Post.objects.all()
    paginator = Paginator(posts, 6)
    for page_num in range(1, paginator.num_pages + 1):
        yield {'page': page_num}

def get_posts():
    for post in Post.objects.all():
        yield {'slug': post.slug}


def get_tags():
    for tag in Tag.objects.all():
        yield {'tag': tag.name}


urlpatterns = [

    distill_path('',
                 IndexView.as_view(),
                 name='blog-index',
                 distill_func=get_index,
                 distill_file='index.html'),

    distill_path('pages/page<int:page>.html', 
                 IndexView.as_view(), 
                 name='blog-index-paginated', 
                 distill_func=get_paginated_index),

    distill_path('posts/<slug:slug>.html',
                 PostView.as_view(),
                 name='blog-post',
                 distill_func=get_posts),

    distill_path('tags/<slug:tag>.html',
                 TagView.as_view(),
                 name='blog-tag',
                 distill_func=get_tags),
    
    distill_path('contact.html',
                 ContactView.as_view(),
                 name='contact',
                 distill_func=get_contact,
                 distill_file='contact.html'),
]

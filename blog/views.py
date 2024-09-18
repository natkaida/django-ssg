from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from .models import Post, Tag



class IndexView(ListView):
    template_name = 'index.html'
    model = Post
    allow_empty = False
    ordering = '-created'
    context_object_name = 'posts'
    paginate_by = 6

class PostView(DetailView):
    template_name = 'post.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        prev_post = Post.objects.filter(created__lt=post.created).order_by('-created').first()
        next_post = Post.objects.filter(created__gt=post.created).order_by('created').first()
        context['prev_post'] = prev_post
        context['next_post'] = next_post
        return context


class TagView(ListView):
    template_name = 'tag.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        return Post.objects.filter(tags__name=self.kwargs['tag']).prefetch_related('tags')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = get_object_or_404(Tag, name=self.kwargs['tag'])
        return context


class ContactView(TemplateView):
    template_name = 'contact.html'
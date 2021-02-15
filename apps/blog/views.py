from django.views.generic import ListView, DetailView

from .models import BlogPost


class BlogListView(ListView):
    model = BlogPost
    template_name = 'home.html'
    context_object_name = 'blog_posts'


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blog-post-detail.html'
    context_object_name = 'blog_post'

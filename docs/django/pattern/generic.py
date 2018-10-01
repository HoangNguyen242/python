from django.views import generic
from .models import Post


class PostListView(generic.ListView):
    model = Post

class PostDetailView(generic.DetailView):
    model = Post

class PostCreateView(generic.CreateView):
    model = Post
    fields = ('title', 'body', 'published', 'date')

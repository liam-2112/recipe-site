from django.shortcuts import render
from django.views import generic
from .models import Post

class PostList(generic.ListView):
    queryset = Post.objects.all().filter(status=1)
    template_name = "home/index.html"
    paginate_by = 6
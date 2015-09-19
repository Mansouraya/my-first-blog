from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.contrib.auth.models import User

def post_list (request):
    posts = Post.objects.filter(author=User.objects.get(username="mansouraya"))
    username = request.user.username

    return render(request, 'blog/post_list.html', {})

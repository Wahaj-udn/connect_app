# connect_app/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Post
from django.core.paginator import Paginator

@login_required
def explore_page(request):
    posts_list = Post.objects.all()

    paginator = Paginator(posts_list, 10)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    context = {
        'posts': posts
    }
    return render(request, 'explore.html', context)

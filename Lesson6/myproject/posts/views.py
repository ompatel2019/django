from django.shortcuts import render, get_object_or_404
from . models import Post

# View for listing all posts
def posts_list(request): 
    posts = Post.objects.all().order_by('-date')    
    return render(request, 'posts/posts_list.html', {'posts': posts})

# View for displaying a single post based on slug
def post_page(request, slug):
    post = get_object_or_404(Post, slug=slug) 
    return render(request, 'posts/post_page.html', {'post': post})

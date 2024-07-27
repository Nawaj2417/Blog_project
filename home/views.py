from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.urls import reverse
from .models import Blog, Category

def index(request):
    post = Blog.objects.order_by('-id')
    main_post = Blog.objects.order_by('-id').filter(Main_post=True)[0:1]
    recent_news = Blog.objects.filter(section='Recent').order_by('-id')[:5]
    category = Category.objects.all()
    blog_cat = Category.objects.all()
    context = {
        'post' : post,
        'recent_news': recent_news,
        'category' : category,
        'main_post' : main_post,
        'blog_cat' : blog_cat
    }
    


    return render(request, 'index.html',context)
from django.shortcuts import render, get_object_or_404, redirect
from .models import Comment
def blog_detail(request, slug):
    posts = Blog.objects.order_by('-id')[:5]
    if not posts:
        raise Http404
    
    category = Category.objects.all()
    recent_news = Blog.objects.filter(section='Recent_news').order_by('-id')[:5]
    share_url = request.build_absolute_uri(reverse('blog_detail', args=[slug]))
    post = get_object_or_404(Blog, blog_slug=slug)

    comments = Comment.objects.filter(blog_id=post.id).order_by('-date')   
    # Handling the comment section here.


    
    context = {
        'post': post,
        'share_url': share_url,
        'posts': posts,
        'category': category,
        'Recent_news': recent_news, 
        'comments': comments 
    }

    return render(request, "blog_detail.html", context)


def category(request, slug):

       cat = Category.objects.all()
       blog_cat = Category.objects.filter(slug=slug)
       context = {
       'cat' : cat,
       'active_category' :slug,
       'blog_cat' : blog_cat,              
       }

        
       return render(request, 'category.html', context)

def add_comment(request,slug):
     
    if request.method == 'POST':
        post = get_object_or_404(Blog, blog_slug = slug)
        name = request.POST.get('InputName')
        email = request.POST.get('InputEmail')
        website = request.POST.get('InputWeb')
        comment_text = request.POST.get('InputComment')
        parent_id = request.POST.get('parent_id')
        parent_comment = None
        
        if parent_id:
            parent_comment = get_object_or_404(Comment, id=parent_id)

        Comment.objects.create(
            post= post,
            name=name,
            email=email,
            website=website,
            comment=comment_text,
            parent=parent_comment
        )
        return redirect("blog_detail",slug=post.blog_slug)
    return redirect('blog_detail')
    
 

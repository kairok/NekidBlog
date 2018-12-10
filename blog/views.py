from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.views.generic import View

#from .utils import ObjectDetailMixin
# Create your views here.
from .models import *
from .forms import *




def user_posts(request, name):
   # user = User.objects.filter(username=name)
    news = News.objects.filter(user__username=name).order_by('-created')
    #user = User.objects.all()
    return render(request, "blog/user_posts.html", {"news": news})


def news_list(request):
    #news = News.objects.all().order_by('-created')
    #user2 = User.objects.filter(username='Sasha')

    news = News.objects.filter(user=request.user).order_by('-created')
    user = User.objects.all()
    return render(request, "blog/index.html", {"news":news, "useers":user})

class PostDetail(View):
    model = News
    template = 'blog/post_detail.html'
    def get(self, request, slug):
        post = get_object_or_404(News, slug__iexact=slug)
        return render(request, 'blog/post_detail.html', context={'post': post})


def Sign_user(request):
    #news = News.objects.all().order_by('-created')
    #user2 = User.objects.filter(username='Sasha')

    news = News.objects.filter(user=request.user).order_by('-created')
    user = User.objects.all()
    return render(request, "blog/index.html", {"news":news, "useers":user})


def news_detail(request):
   # new = get_object_or_404(News)
    if request.method=="POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            #form.new = new
            form.save()
            return redirect('list_news')
    else:

        form = PostForm()
    return render(request, "blog/post_detail.html",
                  {  "form":form})
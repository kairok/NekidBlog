from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.views.generic import View
from django.core.mail import send_mail, BadHeaderError

#from .utils import ObjectDetailMixin

from .models import *
from .forms import *


user_start=User.objects.get(pk=1)


class User_Posts(View):
    model = News
    template = 'blog/user_posts.html'
    def get(self, request, name):
        news = News.objects.filter(blog__user__username__exact=name)
        return render(request, "blog/user_posts.html", {"news": news, "name": name})



class News_Lists(View):
    model = News
    template = 'blog/index.html'
    def get(self, request):
        whos = Signed.objects.get(who=user_start)
        # news = News.objects.filter(blog=blogs).order_by('-created')
        news = News.objects.filter(blog__user__exact=user_start).order_by('-created')
        signed = News.objects.filter(blog__user__in=whos.to.all()).order_by('-created')
        user = User.objects.all()
        return render(request, "blog/index.html", {"news": news, "useers": user, "signed": signed})



class Sign_User(View):
    model = News
    template = 'blog/index.html'
    def get(self, request, name):
        us = User.objects.get(username=name)
        Signed.objects.get(who=user_start).to.add(us)
        whos = Signed.objects.get(who=user_start)

        news = News.objects.filter(blog__user__exact=user_start).order_by('-created')
        signed = News.objects.filter(blog__user__in=whos.to.all()).order_by('-created')
        user = User.objects.all()
        return render(request, "blog/index.html", {"news": news, "useers": user, "signed": signed})



class Add_post(View):
    model = News
    template = 'blog/post_detail.html'
    def post(self, request):
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                send_mail('Subject here', 'Here is the message.', 'from@example.com',
                          ['kairo@list.ru'], fail_silently=False)
                # form.user = request.user
                # form.new = new
                form.save()
                return redirect('list_news')
        else:

            form = PostForm()
        return render(request, "blog/post_detail.html",
                      {"form": form})


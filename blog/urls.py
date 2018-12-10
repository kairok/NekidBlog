
from django.urls import path
from . import views


urlpatterns = [
    path('', views.news_list, name="list_news"),
    path('add', views.news_detail, name="add_post"),
    path('users/<str:name>/', views.user_posts, name="user_posts"),
]

from django.urls import path
from . import views


urlpatterns = [
    path('', views.News_Lists.as_view(), name="list_news"),
    path('add', views.Add_post.as_view(), name="add_post"),
    path('users/<str:name>/', views.User_Posts.as_view(), name="user_posts"),
    path('sign/<str:name>/', views.Sign_User.as_view(), name="signed_user"),
]
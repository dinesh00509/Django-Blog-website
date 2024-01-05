from django.urls import path
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    path('post/<int:pk>/like/', views.like, name='like'),
    path('post/<int:pk>/unlike/', views.like_remove, name='unlike'),
     path('post/<int:pk>/comment/', views.PostDetailView.as_view(), name='post-comment'),
     path('comment-like/<int:pk>/', views.comment_like, name='comment-like'),
     path('comment-unlike/<int:pk>/', views.comment_unlike, name='comment-unlike')
     
      

   
]
from typing import Optional
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post,Comment
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import CommentForm




# Create your views here.




def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


    
    


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','image', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','image', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.author = self.request.user
            new_comment.save()
            return redirect('post-detail', pk=post.pk)


    
def like(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user.is_authenticated and request.user not in post.likes.all():
        post.likes.add(request.user)
    return HttpResponseRedirect(reverse('post-detail', args=[str(pk)]))

def like_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user.is_authenticated and request.user not in post.likes.all():
        post.likes.remove(request.user)
    return HttpResponseRedirect(reverse('post-detail', args=[str(pk)]))



def comment_like(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.user.is_authenticated and request.user not in comment.likes.all():
        comment.likes.add(request.user)
    return HttpResponseRedirect(reverse('post-detail', args=[str(comment.post.pk)]))
  
def comment_unlike(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.user.is_authenticated and request.user in comment.likes.all():
        comment.likes.remove(request.user)
    return HttpResponseRedirect(reverse('post-detail', args=[str(comment.post.pk)]))







def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})




    
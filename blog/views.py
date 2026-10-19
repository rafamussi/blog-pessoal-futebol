from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import CommentForm, PostForm
from .models import Category, Comment, Post


class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')


@login_required
def comment_create(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                post=post, author=request.user, text=form.cleaned_data['text']
            )
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {'form': form, 'post': post})


class CategoryListView(ListView):
    model = Category


def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    context = {'post_list': category.post_set.all(), 'category': category}
    return render(request, 'blog/post_list.html', context)

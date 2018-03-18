# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from .models import Post, Comment
from .filters import PostFilter
from django.shortcuts import get_object_or_404
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
import logging
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Get an instance of a logger
logger = logging.getLogger(__name__)


def go_to_signup(request):
    return redirect('signup')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('post_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required
def post_list(request):
    # TODO: Include paginator
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts_filter = PostFilter(request.GET, queryset=posts)

    # https: // stackoverflow.com / questions / 44048156 / django - filter - use - paginations

    paginator = Paginator(posts_filter.qs, 4)  # Show 4 posts per page

    page = request.GET.get('page')
    # Include paginator https://docs.djangoproject.com/en/1.8/topics/pagination/

    try:
        # If page is not an integer display first page
        posts_pag = paginator.page(page)
    except PageNotAnInteger:
        posts_pag = paginator.page(1)
    except EmptyPage:
        posts_pag = paginator.page(paginator.num_pages)

    # posts_filter object has a form attribute
    # posts_pag is a paginator object. It doesn't have a form attribute so we cannot render the form.
    # We must pass through parameters posts_filter to render the form and posts_pag to render the pagination

    return render(request, 'blog/post_list.html', {'posts': posts_pag, 'posts_form': posts_filter})


@login_required
def post_detail(request, pk, username):
    post = get_object_or_404(Post, pk=pk)
    user = User.objects.get(username=username)

    # New
    post_id = post.pk
    liked = False
    if request.session.get('has_liked_'+str(post_id), liked):
        liked = True
        print("liked {}_{}".format(liked, post_id))

    context = {'post': post, 'liked': liked, 'username': user.username}

    return render(request, 'blog/post_detail.html', context)

@login_required
def post_new(request, username):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk, username=request.user.username)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form, 'username': request.user.username})

@login_required
def post_edit(request, pk, username):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk, username=request.user.username)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_draft_list(request, username):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts, 'username': request.user.username})

@login_required
def post_publish(request, pk, username):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk, username=request.user.username)

@login_required
def post_remove(request, pk, username):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

@login_required
def add_comment_to_post(request):

    user = User.objects.get(username=request.user.username)

    if request.method == 'POST':
        post = get_object_or_404(Post, pk=request.POST['post_id'])

        comment = Comment(author=user.username, text=request.POST['text'], post_id=post.pk)
        comment.save()

    liked = False
    if request.session.get('has_liked_' + str(request.POST['post_id']), liked):
        liked = True

    context = {'post': post, 'liked': liked, 'username': user.username}

    return render(request, 'blog/post_detail.html', context)

@login_required
def click_add_comment(request):

    return HttpResponse(request, 'blog/post_detail.html')

# New like logic
def like_count_blog(request):
    liked = False
    if request.method == 'GET':
        post_id = request.GET['post_id']
        post = Post.objects.get(id=int(post_id))
        if request.session.get('has_liked_'+post_id, liked):
            print("unlike")
            if post.likes > 0:
                likes = post.likes - 1
                try:
                    del request.session['has_liked_'+post_id]
                except KeyError:
                    print("keyerror")
        else:
            print("like")
            request.session['has_liked_' + post_id] = True
            likes = post.likes + 1

    post.likes = likes
    post.save()
    return HttpResponse(likes, liked)


@login_required
def comment_approve(request, pk, username):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk, username=request.user.username)


@login_required
def comment_remove(request, pk, username):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk, username=request.user.username)


@login_required
def get_user_profile(request, username):
    user = User.objects.get(username=username)
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    return render(request, 'blog/user_profile.html', {"user": user, "posts": posts})



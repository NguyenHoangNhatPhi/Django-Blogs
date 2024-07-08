from django.shortcuts import render, redirect, get_object_or_404
from bs4 import BeautifulSoup
import requests
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from a_posts.models import Post, Tag, Comment
from a_posts.forms import PostCreateForm, PostEditForm, CommentCreateForm


def home_view(request, tag=None):
    if tag:
        posts = Post.objects.prefetch_related("tags").filter(tags__slug=tag)
        tag = get_object_or_404(Tag, slug=tag)
    else:
        posts = Post.objects.prefetch_related("tags").all()

    categories = Tag.objects.all()

    context = {"posts": posts, "categories": categories, "tag": tag}

    return render(request, "a_posts/home.html", context)


@login_required
def post_create_view(request):
    form = PostCreateForm()

    if request.method == "POST":
        form = PostCreateForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)

            website = requests.get(form.data["url"])
            sourcecode = BeautifulSoup(website.text, "html.parser")
            find_image = sourcecode.select(
                'meta[content^="https://live.staticflickr.com/"]'
            )
            image = find_image[0]["content"]

            find_title = sourcecode.select("h1.photo-title")
            title = find_title[0].text.strip()

            find_artist = sourcecode.select("a.owner-name")
            artist = find_artist[0].text.strip()

            post.title = title
            post.image = image
            post.artist = artist
            post.author = request.user

            post.save()
            form.save_m2m()

            return redirect("home")

    return render(request, "a_posts/post_create.html", {"form": form})


@login_required
def post_delete_view(request, pk):
    post = get_object_or_404(Post, id=pk, author=request.user)

    if request.method == "POST":
        post.delete()
        messages.success(request, "Post deleted")
        return redirect("home")

    return render(request, "a_posts/post_delete.html", {"post": post})


@login_required
def post_edit_view(request, pk):
    post = get_object_or_404(Post, id=pk, author=request.user)
    form = PostEditForm(instance=post)

    if request.method == "POST":
        form = PostEditForm(request.POST, instance=post)

        if form.is_valid():
            form.save()
            messages.success(request, "Post updated")
            return redirect("home")

    context = {"post": post, "form": form}

    return render(request, "a_posts/post_edit.html", context)


def post_page_view(request, pk):
    post = get_object_or_404(Post, id=pk)
    comments = Comment.objects.prefetch_related("author").filter(parent_post=post)
    commentform = CommentCreateForm()
    context = {"post": post, "commentform": commentform, "comments": comments}

    return render(request, "a_posts/post_detail.html", context)


def comment_sent(request, pk):
    post = get_object_or_404(Post, id=pk)

    if request.method == "POST":
        form = CommentCreateForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.parent_post = post
            comment.save()

    return redirect("post-detail", post.id)

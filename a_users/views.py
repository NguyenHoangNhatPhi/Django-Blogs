from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404

from a_users.models import Profile
from a_users.forms import ProfileForm


def profile_view(request, username=None):
    if username:
        profile = get_object_or_404(User, username=username).profile
    else:
        try:
            profile = request.user.profile
        except:
            return redirect("http://127.0.0.1:8000/accounts/login/")
    return render(request, "a_users/profile.html", {"profile": profile})


def profile_edit_view(request):
    form = ProfileForm(instance=request.user.profile)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if form.is_valid():
            form.save()
            return redirect("profile")

    return render(request, "a_users/profile_edit.html", {"form": form})

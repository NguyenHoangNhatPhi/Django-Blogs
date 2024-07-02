from django.shortcuts import render

from a_users.models import Profile


def profile_view(request):
    profile = request.user.profile

    return render(request, "a_users/profile.html", {"profile": profile})

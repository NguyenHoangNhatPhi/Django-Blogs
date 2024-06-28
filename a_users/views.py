from django.shortcuts import render

def profile_view(request):
    return render(request, "a_users/profile.html")

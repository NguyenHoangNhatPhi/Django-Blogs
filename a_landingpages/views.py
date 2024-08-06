from django.shortcuts import render, redirect

from a_landingpages.forms import AccessForm
from a_landingpages.models import LandingPage


def maintenance_page(request):
    return render(request, "a_landingpages/maintenance.html")


def locked_page(request):
    form = AccessForm()

    if request.method == "POST":
        form = AccessForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data.get("password")
            try:
                access_code = LandingPage.objects.get(name="Staging").access_code
                if access_code == password:
                    request.session["staging_access"] = True
                    return redirect("home")
            except:
                pass

    return render(request, "a_landingpages/locked.html", {"form": form})

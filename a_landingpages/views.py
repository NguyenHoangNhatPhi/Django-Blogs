from django.shortcuts import render


def maintenance_page(request):
    return render(request, "a_landingpages/maintenance.html")

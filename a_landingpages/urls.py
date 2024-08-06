from django.urls import path

from a_landingpages import views

urlpatterns = [
    path("maintenance/", views.maintenance_page,name="maintenance")
]
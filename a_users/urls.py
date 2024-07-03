from django.urls import path

from a_users import views

urlpatterns = [
    path("profile/", views.profile_view, name="profile"),
    path("user/<username>/", views.profile_view, name="userprofile"),
    path("profile-edit/", views.profile_edit_view, name="profile-edit"),
]

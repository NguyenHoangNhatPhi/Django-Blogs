from django.urls import path

from a_users import views

urlpatterns = [
    path("profile/", views.profile_view, name="profile"),
    path("user/<username>/", views.profile_view, name="user-profile"),
    path("profile-edit/", views.profile_edit_view, name="profile-edit"),
    path("profile-delete", views.profile_delete_view, name="profile-delete"),
    path("profile-onboarding/", views.profile_edit_view, name="profile-onboarding"),
    path("profile/verify-email", views.profile_verify_email, name="profile-verify-email"),
]

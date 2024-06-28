from django.urls import path


from a_posts import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("category/<tag>", views.home_view, name="category"),
    path("post-create/", views.post_create_view, name="post-create"),
    path("post-delete/<pk>/", views.post_delete_view, name="post-delete"),
    path("post-edit/<pk>", views.post_edit_view, name="post-edit"),
    path("post-detail/<pk>", views.post_page_view, name="post-detail"),
]

from django.urls import path


from a_posts import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("category/<tag>/", views.home_view, name="category"),
    path("post-create/", views.post_create_view, name="post-create"),
    path("post-delete/<pk>/", views.post_delete_view, name="post-delete"),
    path("post-edit/<pk>/", views.post_edit_view, name="post-edit"),
    path("post-detail/<pk>/", views.post_page_view, name="post-detail"),
    path("comment-sent/<pk>/", views.comment_sent, name="comment-sent"),
    path("comment-delete/<pk>/", views.comment_delete_view, name="comment-delete"),
    path("reply-sent/<pk>/", views.reply_send, name="reply-sent"),
    path("reply-delete/<pk>/", views.reply_delete_view, name="reply-delete"),
    path("post-like/<pk>/", views.like_post, name="like-post"),
    path("comment-like/<pk>/", views.like_comment, name="like-comment"),
    path("reply-like/<pk>/", views.like_reply, name="like-reply"),
]

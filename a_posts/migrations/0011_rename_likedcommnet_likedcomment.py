# Generated by Django 5.0.6 on 2024-07-12 07:56

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("a_posts", "0010_likedcommnet_comment_likes"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name="LikedCommnet",
            new_name="LikedComment",
        ),
    ]

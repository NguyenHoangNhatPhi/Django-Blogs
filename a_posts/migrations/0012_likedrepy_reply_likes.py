# Generated by Django 5.0.6 on 2024-07-15 07:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("a_posts", "0011_rename_likedcommnet_likedcomment"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="LikedRepy",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "reply",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="a_posts.reply"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="reply",
            name="likes",
            field=models.ManyToManyField(
                related_name="likedreplies",
                through="a_posts.LikedRepy",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]

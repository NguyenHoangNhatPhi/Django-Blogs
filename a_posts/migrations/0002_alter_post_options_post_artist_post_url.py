# Generated by Django 5.0.6 on 2024-06-24 08:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("a_posts", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="post",
            options={"ordering": ["-created"]},
        ),
        migrations.AddField(
            model_name="post",
            name="artist",
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name="post",
            name="url",
            field=models.URLField(max_length=500, null=True),
        ),
    ]

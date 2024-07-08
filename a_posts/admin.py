from django.contrib import admin

from a_posts.models import *

admin.site.register([Post, Tag, Comment, Reply])

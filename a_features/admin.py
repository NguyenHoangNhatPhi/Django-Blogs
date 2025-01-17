from django.contrib import admin
from a_features.models import Feature


class FeatureAdmin(admin.ModelAdmin):
    list_display = ("name", "id", "developer", "staging_enabled", "production_enabled")


admin.site.register(Feature, FeatureAdmin)

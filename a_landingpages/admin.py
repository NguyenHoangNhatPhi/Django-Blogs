from django.contrib import admin

from a_landingpages.models import LandingPage


class LandingPageAdmin(admin.ModelAdmin):
    list_display = ("name", "is_enabled", "access_code")


admin.site.register(LandingPage, LandingPageAdmin)

from django.contrib import admin

from .models import Feedback, SubwayStation


class SubwayStationAdmin(admin.ModelAdmin):
    list_display = (
        "stop_name",
        "lat",
        "lon",
        "line",
        "ada",
    )


admin.site.register(SubwayStation, SubwayStationAdmin)
admin.site.register(Feedback)

from django.contrib import admin

from .models import *

admin.site.register(Project)
admin.site.register(Milestone)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "priority", "status")
    search_fields = ("title",)
    list_filter =  ("priority", "status")
    class Meta:
        ordering = ("priority")

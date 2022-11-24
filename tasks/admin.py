from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    # fieldsets = [
    #     (None, {'fields': ['title']}),
    #     (None, {'fields': ['description']}),
    #     (None, {'fields': ['completed']}),
    #     (None, {'fields': ['important']}),
    #     (None, {'fields': ['user']}),
    # ]
    readonly_fields = ('created', 'completed',)
    list_display = ('title', 'created', 'was_published_recently', 'created_by')
    list_filter = ['title', 'created', 'completed']
    search_fields = ['title']


admin.site.register(Task, TaskAdmin)

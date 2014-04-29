from django.contrib import admin
from todo import models


class TodoAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'status', 'is_finished']

admin.site.register(models.Todo, TodoAdmin)
admin.site.register(models.TodoCategory)

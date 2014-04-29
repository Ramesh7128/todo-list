from django.contrib import admin
from todo import models


class TodoAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'status']


admin.site.register(models.Todo, TodoAdmin)
admin.site.register(models.TodoCategory)

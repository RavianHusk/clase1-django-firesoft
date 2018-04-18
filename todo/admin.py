from django.contrib import admin
from .models import TodoModel
# Register your models here.


@admin.register(TodoModel)
class TodoModelModelAdmin(admin.ModelAdmin):
    model = TodoModel
    list_display = ('title', 'description', 'created')
    search_fields = ('title', 'description')
    list_display_links = ('title', 'description')
    list_filter = ('created',)

from django.contrib import admin
from .models import Todo, User

# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

admin.site.register(Todo, TodoAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'age')
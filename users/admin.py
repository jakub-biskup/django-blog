from django.contrib import admin
from .models import Profile


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Profile)

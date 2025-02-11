from django.contrib import admin
from app_teaching.models import *

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'published'
    empty_value_display = '-empty-'
    list_display = ['title', 'published']
    list_filter = ['tags', 'published']
    search_fields = ['title', 'content']
admin.site.register(Post,PostAdmin)

class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
admin.site.register(Tag,TagAdmin)
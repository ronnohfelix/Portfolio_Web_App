from django.contrib import admin
from .models import Tag, Project, Image

# Register your models here.

class ImageInline(admin.TabularInline):
    model = Image
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'link')
    inlines = [ImageInline]
    search_fields = ['title', 'description']
    list_filter = ['tags']

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']

admin.site.register(Tag, TagAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Image)
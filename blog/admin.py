# Register your models here.
from django.contrib import admin

from models import Article, Category, Tag


class ArticleAdmin(admin.ModelAdmin):
    def make_published(self, query):
        query.update(satus='p')

    make_published.short_description = "Mark selected Article as published"

    list_display = ['title', 'status', 'category', 'views', 'created_time', 'last_modified_time']
    list_filter = ('status', 'category')
    date_hierarchy = 'created_time'
    list_editable = ['status', 'views']
    search_fields = ['title']
    ordering = ['title']
    actions = [make_published]


class CategoryAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_time'
    list_display = ['name', 'order', 'created_time', 'last_modified_time']
    list_editable = ['order']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag)

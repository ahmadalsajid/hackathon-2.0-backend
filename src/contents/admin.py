from django.contrib import admin

from contents.models import Author, Content, Tag, ContentTag


class AuthorAdmin(admin.ModelAdmin):
    list_per_page = 30
    list_display = ('name', 'username', 'unique_id')


class ContentAdmin(admin.ModelAdmin):
    list_per_page = 30
    list_display = ('unique_id', 'title')


class TagAdmin(admin.ModelAdmin):
    list_per_page = 30
    list_display = ('name', 'description')


class ContentTagAdmin(admin.ModelAdmin):
    list_per_page = 30
    list_display = ('content', 'tag')


admin.site.register(Author, AuthorAdmin)
admin.site.register(Content, ContentAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(ContentTag, ContentTagAdmin)
from django.contrib import admin

from plugs_post import models


class PostAdmin(admin.ModelAdmin):
    """
    Post Model Admin
    """
    list_display = ('name', 'author', 'created', 'updated')
    list_filter = ('author', )
    search_fields = ('name', )
    readonly_fields = ('slug', 'created', 'updated')


class PostSectionAdmin(admin.ModelAdmin):
    """
    Post Section Model Admin
    """
    list_display = ('name', 'slug', 'created', 'updated')
    search_fields = ('name', )
    readonly_fields = ('slug', 'created', 'updated')


admin.site.register(models.Post, PostAdmin)
admin.site.register(models.PostSection, PostSectionAdmin)

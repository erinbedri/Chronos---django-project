from django.contrib import admin

from chronos.web.models import Watch, Comment, Post


@admin.register(Watch)
class WatchAdmin(admin.ModelAdmin):
    list_display = ('owner', 'brand', 'model', 'year', 'condition')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'watch', 'created_on')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_on')
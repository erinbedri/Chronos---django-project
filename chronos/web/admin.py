from django.contrib import admin

from chronos.web.models import Watch, WatchComment, Post, PostComment


@admin.register(Watch)
class WatchAdmin(admin.ModelAdmin):
    list_display = ('owner', 'brand', 'model', 'year', 'condition')


@admin.register(WatchComment)
class WatchCommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'watch', 'created_on')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_on')


@admin.register(PostComment)
class PostCommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'created_on')
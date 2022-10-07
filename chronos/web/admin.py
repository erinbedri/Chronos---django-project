from django.contrib import admin

from chronos.web.models import Watch, Comment


@admin.register(Watch)
class WatchAdmin(admin.ModelAdmin):
    list_display = ('owner', 'brand', 'model', 'year', 'condition')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'watch', 'created_on')

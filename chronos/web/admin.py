from django.contrib import admin

from chronos.web.models import Watch, WatchComment


@admin.register(Watch)
class WatchAdmin(admin.ModelAdmin):
    list_display = ('owner', 'brand', 'model', 'year', 'condition')


@admin.register(WatchComment)
class WatchCommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'watch', 'created_on')



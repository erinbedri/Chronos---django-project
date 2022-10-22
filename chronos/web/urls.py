from django.urls import path, include

from chronos.web import views

urlpatterns = [
    path('', views.show_homepage, name='show homepage'),
    path('accounts/', include('chronos.accounts.urls')),
    path('posts/', include('chronos.posts.urls')),
    path('watches/', include('chronos.watches.urls')),
]

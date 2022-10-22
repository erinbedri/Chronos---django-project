from django.urls import path, include

from chronos.web import views

urlpatterns = [
    path('', views.show_homepage, name='show homepage'),
    path('profile/', include('chronos.accounts.urls')),
    path('post/', include('chronos.post.urls')),
    path('watch/', include('chronos.watch.urls')),
]

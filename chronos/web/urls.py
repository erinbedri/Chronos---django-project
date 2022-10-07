from django.urls import path, include

from chronos.web import views

urlpatterns = [
    path('', views.show_homepage, name='show homepage'),
    path('profile/', include('chronos.user_profile.urls')),
    path('post/', include('chronos.post.urls')),



    path('watch/add/', views.add_watch, name='add watch'),
    path('watch/all/', views.show_dashboard, name='show dashboard'),
    path('watch/details/<int:pk>', views.show_watch, name='show watch'),
    path('watch/edit/<int:pk>', views.edit_watch, name='edit watch'),
    path('watch/delete/<int:pk>', views.delete_watch, name='delete watch'),
    path('watch/like/<int:pk>', views.like_watch, name='like watch'),
]

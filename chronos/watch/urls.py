from django.urls import path

from chronos.watch import views

urlpatterns = [
    path('watch/add/', views.add_watch, name='add watch'),
    path('watch/all/', views.show_all_watches, name='show dashboard'),
    path('watch/details/<int:pk>', views.show_watch, name='show watch'),
    path('watch/edit/<int:pk>', views.edit_watch, name='edit watch'),
    path('watch/delete/<int:pk>', views.delete_watch, name='delete watch'),
    path('watch/like/<int:pk>', views.like_watch, name='like watch'),
]

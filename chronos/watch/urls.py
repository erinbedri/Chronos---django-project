from django.urls import path

from chronos.watch import views

urlpatterns = [
    path('add/', views.add_watch, name='add watch'),
    path('all/', views.show_all_watches, name='show dashboard'),
    path('details/<int:pk>', views.show_watch, name='show watch'),
    path('edit/<int:pk>', views.edit_watch, name='edit watch'),
    path('delete/<int:pk>', views.delete_watch, name='delete watch'),
    path('like/<int:pk>', views.like_watch, name='like watch'),
]

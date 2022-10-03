from django.urls import path

from chronos.web import views

urlpatterns = [
    path('', views.show_homepage, name='show homepage'),

    path('profile/register/', views.register_profile, name='register profile'),
    path('profile/show/', views.show_profile, name='show profile'),
    path('profile/edit/', views.edit_profile, name='edit profile'),
    path('profile/delete/', views.delete_profile, name='delete profile'),

    path('watch/add/', views.add_watch, name='add watch'),
    path('watch/all/', views.show_dashboard, name='show dashboard'),
    path('watch/details/<int:pk>', views.show_watch, name='show watch'),
    path('watch/edit/<int:pk>', views.edit_watch, name='edit watch'),
    path('watch/delete/<int:pk>', views.delete_watch, name='delete watch'),
]
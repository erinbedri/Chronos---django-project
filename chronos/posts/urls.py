from django.urls import path

from chronos.posts import views

urlpatterns = [
    path('details/<int:pk>', views.show_post, name='show post'),
]
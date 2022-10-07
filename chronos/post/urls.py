from django.urls import path

from chronos.post import views

urlpatterns = [
    path('post/details/<int:pk>', views.show_post, name='show post'),
]
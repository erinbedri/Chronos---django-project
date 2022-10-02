from django.urls import path

from chronos.web import views

urlpatterns = [
    path('', views.show_homepage, name='show homepage'),
    path('register/', views.register_profile, name='register profile'),
]
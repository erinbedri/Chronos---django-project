from django.urls import path

from chronos.accounts import views


urlpatterns = [
    path('register/', views.register_profile, name='register profile'),
    path('login/', views.login_profile, name='login profile'),
    path('logout/', views.logout_profile, name='logout profile'),
    path('show/', views.show_profile, name='show profile'),
    path('edit/', views.edit_profile, name='edit profile'),
    path('delete/', views.delete_profile, name='delete profile'),

    # path('register/', RegisterView.as_view(), name='register profile'),
]

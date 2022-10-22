from django.urls import path

from chronos.accounts import views


urlpatterns = [
    path('register/', views.register_account, name='register account'),
    path('login/', views.login_user, name='login user'),
    path('logout/', views.logout_user, name='logout user'),
    path('show/', views.show_account, name='show account'),
    path('edit/', views.edit_account, name='edit account'),
    path('delete/', views.delete_account, name='delete account'),

    # path('register/', RegisterView.as_view(), name='register profile'),
]

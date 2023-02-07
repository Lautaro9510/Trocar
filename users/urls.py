from django.contrib.auth.views import LogoutView
from django.urls import path

from users.views import login_view, register, update_user, update_user_profile, show_user

urlpatterns = [
    path('login/', login_view),
    path('logout/', LogoutView.as_view(template_name = 'users/logout.html')),
    path('register/', register),
    path('update/', update_user),
    path('update/profile/', update_user_profile, name='update_profile'),
    path('show_user/', show_user)
]
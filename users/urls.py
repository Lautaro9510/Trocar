from django.contrib.auth.views import LogoutView
from django.urls import path

from users.views import login_view, register, update_user, update_user_profile, show_user, UserList, edit_user, edit_profile_user, eliminate_user

urlpatterns = [
    path('login/', login_view),
    path('logout/', LogoutView.as_view(template_name = 'users/logout.html')),
    path('register/', register),
    path('update/<id>/', update_user),
    path('update/profile/', update_user_profile, name='update_profile'),
    path('show_user/', show_user),
    path('user_list/', UserList.as_view(), name='user_list'),
    path('edit_user/<id>/', edit_user),
    path('edit_profile/<id>/', edit_profile_user),
    path('eliminate_user/<id>/', eliminate_user),
]
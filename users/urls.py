from django.urls import path
import users.views as users

app_name = 'users'

urlpatterns = [
    path('login/', users.LoginLoginView.as_view(), name='login'),
    path('register/', users.RegisterListView.as_view(), name='register'),
    path('profile/', users.ProfileFormView.as_view(), name='profile'),
    path('logout/', users.Logout.as_view(), name='logout'),
]

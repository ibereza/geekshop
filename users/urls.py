from django.urls import path
import users.views as users

app_name = 'users'

urlpatterns = [
    path('login/', users.login, name='login'),
    path('register/', users.register, name='register'),
    path('logout/', users.logout, name='logout'),
]

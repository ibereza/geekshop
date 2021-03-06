from django.urls import path
import admins.views as admins

app_name = 'admins'

urlpatterns = [
    path('', admins.index, name='index'),

    path('users/', admins.UserListView.as_view(), name='admins_user'),
    path('users-create/', admins.UserCreateView.as_view(), name='admins_user_create'),
    path('users-update/<int:pk>/', admins.UserUpdateView.as_view(), name='admins_user_update'),
    path('users-delete/<int:pk>/', admins.UserDeleteView.as_view(), name='admins_user_delete'),

    path('categories/read/', admins.CategoriesListView.as_view(), name='admins_categories'),
    path('category/create/', admins.CategoryCreateView.as_view(), name='admins_category_create'),
    path('category/update/<int:pk>/', admins.CategoryUpdateView.as_view(), name='admins_category_update'),
    path('category/delete/<int:pk>/', admins.CategoryDeleteView.as_view(), name='admins_category_delete')
]

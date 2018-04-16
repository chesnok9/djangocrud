from django.urls import path

from users.views import UserList, UserDetailView, UserCreateView, UserUpdateView, UserDeleteView, exportToCSV

app_name='users'
urlpatterns = [
    path('', UserList.as_view(), name='user-list'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('user/create', UserCreateView.as_view(), name='user-create'),
    path('user/update/<int:pk>/', UserUpdateView.as_view(), name='user-update'),
    path('user/delete/<int:pk>/', UserDeleteView.as_view(), name='user-delete'),
    path('export', exportToCSV, name='user-export'),
]
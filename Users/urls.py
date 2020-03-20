from django.urls import path
from Users.views import UserListView

urlpatterns = [
    path('', UserListView.as_view(), name='users'),
]

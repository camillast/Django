from django.urls import path
from CustomUser.views import UserListView

urlpatterns = [
    path('', UserListView.as_view(), name='users'),
]

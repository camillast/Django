from django.urls import path
from topicslearned.views import TopicsListView

urlpatterns = [
    path('', TopicsListView.as_view(), name='topics'),
]

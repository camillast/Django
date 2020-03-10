from rest_framework.generics import ListCreateAPIView
from topicslearned.models import Topics
from topicslearned.serializers import TopicsSerializer


class TopicsListView(ListCreateAPIView):
    serializer_class = TopicsSerializer

    def get_queryset(self):
        return Topics.objects.all().select_related('owner')


""" class TopicsCreateView(CreateAPIView):
    serializer_class = TopicsSerializer

    def perform_create(self, serializer):
"""

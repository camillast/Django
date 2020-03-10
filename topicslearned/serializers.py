from topicslearned.models import Topics
from rest_framework import serializers


class TopicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topics
        fields = ("id", "title", "content", "pub_date")
        read_only_fields = fields

from django.urls import reverse
from model_bakery import baker
from rest_framework import status
from django.test import TestCase


class TopicsListViewTestCase(TestCase):
    def setUp(self):
        self.topic1 = baker.make('topicslearned.Topics')

    def test_list_topics_success(self):
        response = self.client.get(
            reverse("topics"),
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_objects_success(self):
        response = self.client.get(
            reverse("topics"),
            format="json"
        )
        self.assertCountEqual(
            response.data,
            [
                {
                    "id": self.topic1.id,
                    "owner": self.topic1.ownwe.id,
                    "title": self.topic1.title,
                    "content": self.topic1.content,
                    "pub_date": self.topic1.pub_date
                },
            ],
        )

from django.db import models
from django.conf import settings


class Topics(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='topics', on_delete=models.CASCADE)
    title = models.CharField(max_length=60)
    content = models.TextField()
    pub_date = models.DateTimeField(null=True)

    def __str__(self):
        return f'{self.title} {self.owner}'

import uuid

from django.db import models


class Article(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    title = models.CharField(max_length=256)
    date = models.DateTimeField(auto_now=True)
    image = models.ImageField()
    content = models.TextField()

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title

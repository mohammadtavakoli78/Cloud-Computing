from django.db import models


# Create your models here.


class PrivateNote(models.Model):
    url = models.CharField(max_length=255, null=False, primary_key=True)

    text = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

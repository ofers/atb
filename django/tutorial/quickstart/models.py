from django.db import models


class User(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    pid = models.TextField(unique=True, max_length=255)
    department = models.TextField()


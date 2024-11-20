from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)

class Tag(models.Model):
    # Model Tag (Dados: name)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
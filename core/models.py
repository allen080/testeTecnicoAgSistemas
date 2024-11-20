from django.db import models

class Tag(models.Model):
    # Model Tag (Dados: name)
    name = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100, default="")
    content = models.TextField(default="Test")
    created_at = models.DateTimeField(auto_now_add=True)
    # Post has one or more tags and Tag has one or more posts
    tags = models.ManyToManyField(Tag) 

    def __str__(self):
        return self.title


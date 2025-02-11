from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    example_code = models.TextField(blank=True)
    views = models.PositiveIntegerField(default=0)
    tags = models.ManyToManyField('Tag', blank=True)
    published = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['published']

    def increment_views(self):
        self.views += 1
        self.save()

    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name

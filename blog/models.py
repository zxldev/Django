from django.db import models

# Create your models here.
class Article(models.Model):
    using = 'blog'
    content = models.TextField()
    title = models.CharField(max_length=100)
    categroy = models.CharField(max_length=20)


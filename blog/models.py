from django.db import models

# Create your models here.
class Tag(models.Model):
    caption = models.CharField(max_length=100)

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

class Post(models.Model):
    title = models.CharField(max_length=255)
    excerpt = models.ManyToManyField(Tag)
    date = models.DateField(auto_created=True)
    slug = models.SlugField()
    content = models.TextField(max_length=1500)
    
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
      
      

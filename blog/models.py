from django.db import models

# Create your models here.
class Tag(models.Model):
    caption = models.CharField(max_length=100)

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()

class Post(models.Model):
    title = models.CharField(max_length=255)
    excerpt = models.CharField(max_length=150)
    date = models.DateField(auto_created=True, auto_now=True)
    slug = models.SlugField(unique=True)
    image= models.CharField(max_length=100)
    content = models.TextField(max_length=1500)
    
    author = models.ForeignKey(Author,on_delete=models.SET_NULL, null=True, related_name='post_author')
    tags = models.ManyToManyField(Tag)
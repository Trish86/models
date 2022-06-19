from django.db import models
from django.db import Post
# Create your models here.

class blog(models.Model):
    title = models.CharField(max_length=200, unique=True)
    text= models.TextField()
    author = models.ForeignKey(Post, on_delete= models.CASCADE,related_name='blog_posts') 
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text



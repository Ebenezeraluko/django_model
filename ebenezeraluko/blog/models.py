from django.db import models

# Create your models here.

class Post(models.Model):
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Post"
    post_title = models.CharField(max_length=200)
    post_text = models.TextField(max_length=200)
    post_author = models.get_user_model
    created_date = models.DateTimeField    
    published_date = models.DateTimeField                        
    



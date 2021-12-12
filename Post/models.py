from django.db import models
from Profile.models import userprofile

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200,blank=True)
    slug=models.SlugField(max_length=20,null=True)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField(default=False)
    author = models.ForeignKey(userprofile, on_delete=models.CASCADE)
    image=models.ImageField(upload_to="uploads/",)
    
    
    
    

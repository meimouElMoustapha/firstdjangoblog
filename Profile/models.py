from django.db import models
# from django.contrib.auth.models import User
# Create your models here.
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save,pre_save
# from django.utils.text import slugify




User=settings.AUTH_USER_MODEL

class userprofile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    
    bio=models.CharField(max_length=200,blank=True)
    profile_image=models.ImageField(upload_to="uploads/",)
    
    def __str__(self):
        return self.user.username
    
    
    
    
    @receiver(pre_save,sender=User)
    
    def user_presave(sender,instance,*args,**kwargs):
        
            print(instance.username,instance.id)
    
    
    
    @receiver(post_save,sender=User)
    
    def user_created_handler(sender,instance,created,*args,**kwargs):
        if created:
            userprofile.objects.create(user=instance)
            
    post_save.connect(user_created_handler,sender=User)
            
            
    # @receiver(post_save,sender=Post)
    
    # def blog_post_post_save(sender,instance,created,*args,**kwargs):
    #     if not instance.slug:
    #         instance.slug=slugify(instance.title)
    #         instance.save()
        

       
        

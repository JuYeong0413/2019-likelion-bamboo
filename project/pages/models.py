from django.db import models
from imagekit.models import ImageSpecField # 썸네일만드는거
from imagekit.processors import ResizeToFill # 크기조정 추가
from dirtyfields import DirtyFieldsMixin


# Create your models here.
class Post(DirtyFieldsMixin, models.Model):
    objects = models.Manager()
    password = models.CharField(max_length=200)
    content = models.TextField()
    img = models.ImageField(upload_to='image', blank=True)
    comment_count = models.IntegerField(default=0)
    
    is_edited = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def comments(self):
        return Comment.objects.filter(post=self)

    
class Comment(models.Model):
    objects = models.Manager()
    writer = models.CharField(max_length=200)
    message = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



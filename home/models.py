from django.db import models

class Addpost(models.Model):
    event_name=models.CharField(max_length=30)
    data=models.TextField()
    time=models.DateTimeField(auto_now_add=True)
    location=models.CharField(max_length=30)
    image=models.ImageField(upload_to='event_img/')
    is_liked=models.BooleanField(default=False)

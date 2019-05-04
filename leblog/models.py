from django.db import models
from datetime import datetime
# Create your models here.
class Post(models.Model):

    title = models.CharField(max_length=20, help_text='Enter Post Title')
    content = models.TextField(help_text='Post Content')
    publish_date = models.DateTimeField(datetime.now(), editable=True, auto_now_add=True)
    id = models.AutoField(primary_key=True)
    ##image = models.TextField(help_text="Link to Image", null=True)

    class Meta:
        ordering = ['publish_date']

    def __str__(self):
        return self.title

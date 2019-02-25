from django.db import models

# Create your models here.
from django.db import models


# okay, what kind of model do you want to create? Maybe just a kind of simple blog application
class Post(models.Model):
    post_text = models.TextField()
    author = models.CharField(max_length=200, null=True)
    pub_date = models.DateTimeField('date published', null=True)



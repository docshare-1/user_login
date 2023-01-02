from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
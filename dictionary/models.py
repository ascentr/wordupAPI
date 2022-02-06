from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Words(models.Model):
    word = models.CharField(max_length=50)
    meaning = models.TextField(max_length=500)
    owner = models.ForeignKey(User, related_name="wordlist", on_delete=models.CASCADE, null=True )
    created_at = models.DateTimeField(auto_now_add=True)


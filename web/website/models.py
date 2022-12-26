from django.db import models

class webstore(models.Model):
    # id =models.IntegerField(max_length=50, primary_key=True, null=False)
    Name=models.CharField(max_length=100)
    Phone=models.CharField(max_length=60)
    Email=models.CharField(max_length=400)
    Message=models.TextField()

# Create your models here.
#wait let me check all things


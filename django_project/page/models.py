from django.db import models

# Create your models here.
class user_table(models.Model):
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=8)

    def __str__(self):
        return self.name
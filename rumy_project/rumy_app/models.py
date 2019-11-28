from django.db import models

# Create your models here.
class UserModel(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=50)
    age = models.IntegerField()
    bio = models.CharField(max_length=500)

    def __str__(self):
        return f'Username: {self.username} Password: {self.password} Age: {self.age} Bio: {self.bio}'

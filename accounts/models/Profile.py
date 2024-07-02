from django.db import models
from accounts.models import CustomUser

class Profile(models.Model):
    '''
    This Class is for user profile
    '''
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="users", default="user.jpg")
    phone = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.user.email
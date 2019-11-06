from django.db import models

# Create your models here.


class User(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    # Max length of username + #0000
    user_name = models.CharField(max_length=37)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField('Created At')
    ip = models.GenericIPAddressField(default=None, unique=True)
    # TODO: Token Field

    def __str__(self):
        return self.user_name

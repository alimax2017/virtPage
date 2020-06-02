from django.db import models

# Create your models here.
class User(models.Model):
    """User class"""
    last_name=models.CharField(max_length=265)
    first_name=models.CharField(max_length=265)
    email=models.EmailField()


#    def __init__(self, arg):
#        super(, self).__init__()
#        self.arg = arg

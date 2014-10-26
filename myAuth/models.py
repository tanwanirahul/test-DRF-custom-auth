from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    '''
        Profile information for the django user.
    '''
    github = models.CharField(max_length=20)
    user = models.OneToOneField(User, related_name="profile")

    def __unicode__(self):
        '''
            Unicode and String representation.
        '''
        return "%s" % (self.github)

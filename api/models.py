# models.py
from django.db import models
from django.utils.translation import gettext_lazy as _

def upload_to(instance,filename):
   return "posts/{filename}".format(filename=filename)


class Profile(models.Model):
    name = models.CharField(unique=True, max_length=100)
    designation = models.CharField(max_length=100, null=True)
    organisation = models.CharField(max_length=100, null=True)
    # start_date = models.DateField()
    about = models.CharField(max_length=500, blank=True, null=True)
    picture = models.ImageField(_("image"), upload_to=upload_to, default="post/default.png")
    areas_of_interest = models.CharField(max_length=500, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)  # New field for email
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
   

    def __str__(self):
        return self.name

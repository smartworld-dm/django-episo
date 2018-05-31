from django.utils.translation import gettext as _
from django.db import models
from jsonfield import JSONField
import datetime

# Create your models here.
from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=50)
    introduction = models.TextField(default="")
    small_introduction = models.CharField(max_length=50, default="")
    logo_image = models.FileField(default="default.png")
    creation_date = models.DateField(_("Date"), default=datetime.date.today)
    
    def __str__(self):
        """A string representation of the model."""
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, default=0)
    is_featured = models.BooleanField()
    cover_image = models.FileField(default="default.png")
    member_name = models.TextField()
    member_title = models.TextField()
    attribute = models.TextField()
    region = models.TextField()
    category = models.TextField()
    creation_date = models.DateField()
    content = models.TextField()
    is_published = models.BooleanField(default=False)
    free_links = JSONField("free_links")

    def __str__(self):
        """A string representation of the model."""
        return self.title

from django.utils.translation import gettext as _
from django.db import models
from jsonfield import JSONField
import datetime

from brands.models import Brand

class Article(models.Model):
    title               = models.CharField(max_length=200)
    brand               = models.ForeignKey(Brand, on_delete=models.CASCADE, default=0)
    is_featured         = models.BooleanField()
    cover_image         = models.FileField(default="default.png")
    member_name         = models.TextField()
    member_title        = models.TextField()
    attribute           = models.TextField()
    region              = models.TextField()
    category            = models.TextField()
    content             = models.TextField()
    is_published        = models.BooleanField(default=False)
    free_links          = JSONField("free_links")
    creation_date       = models.DateField()

    def __str__(self):
        return self.title

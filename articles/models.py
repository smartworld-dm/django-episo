from django.utils.translation import gettext as _
from django.db import models
from jsonfield import JSONField
from datetime import datetime

from brands.models import Brand

class Article(models.Model):
    title               = models.CharField(default="", max_length=200, null=True, blank=True)
    brand               = models.ForeignKey(Brand, on_delete=models.CASCADE, default=0)
    is_featured         = models.BooleanField(default=False)
    cover_image         = models.FileField(upload_to='', null=True, blank=True)
    member_name         = models.CharField(default="", max_length=200, null=True, blank=True)
    member_title        = models.CharField(default="", max_length=200, null=True, blank=True)
    attribute           = models.CharField(default="", max_length=200, null=True, blank=True)
    region              = models.CharField(default="", max_length=200, null=True, blank=True)
    category            = models.CharField(default="", max_length=200, null=True, blank=True)
    content             = models.TextField(default="", null=True, blank=True)
    is_published        = models.BooleanField(default=False)
    free_links          = JSONField("free_links", default=[], null=True, blank=True)
    creation_date       = models.DateTimeField(default=datetime.now, null=True, blank=True)

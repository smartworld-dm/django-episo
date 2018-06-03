from django.utils.translation import gettext as _
from django.db import models
from jsonfield import JSONField
from datetime import datetime

from brands.models import Brand

class Article(models.Model):
    title               = models.CharField(max_length=200)
    brand               = models.ForeignKey(Brand, on_delete=models.CASCADE, default=0)
    is_featured         = models.BooleanField(default=False)
    cover_image         = models.FileField(upload_to='uploads/', default="default.png")
    member_name         = models.TextField(null=True, blank=True)
    member_title        = models.TextField(null=True, blank=True)
    attribute           = models.TextField(null=True, blank=True)
    region              = models.TextField(null=True, blank=True)
    category            = models.TextField(null=True, blank=True)
    content             = models.TextField(null=True, blank=True)
    is_published        = models.BooleanField(default=False)
    free_links          = JSONField("free_links", default={ "key": "value" }, null=True, blank=True)
    creation_date       = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title

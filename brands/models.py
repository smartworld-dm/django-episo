from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django.db import models
from jsonfield import JSONField
from datetime import datetime

class Brand(models.Model):
    user                    = models.OneToOneField(User, on_delete=models.CASCADE, default=0)
    name                    = models.CharField(max_length=50, null=True, blank=True)
    name_slug               = models.CharField(max_length=50, null=True, blank=True)
    logo_image              = models.FileField(upload_to='uploads/', default="default.png", null=True, blank=True)
    cover_image             = models.FileField(upload_to='uploads/', default="default.png", null=True, blank=True)
    introduction            = models.TextField(null=True, blank=True)
    small_introduction      = models.CharField(max_length=50, null=True, blank=True)
    facebook_url            = models.CharField(max_length=200, null=True, blank=True)
    twitter_url             = models.CharField(max_length=200, null=True, blank=True)
    instagram_url           = models.CharField(max_length=200, null=True, blank=True)
    company_name            = models.CharField(max_length=200, null=True, blank=True)
    company_representative  = models.CharField(max_length=200, null=True, blank=True)
    company_address         = models.CharField(max_length=200, null=True, blank=True)
    company_website         = models.CharField(max_length=200, null=True, blank=True)
    company_founding_date   = models.DateField(_("Date"), default=datetime.today)
    company_sales_offices   = models.TextField(null=True, blank=True)
    company_introduction    = models.TextField(null=True, blank=True)
    free_links              = JSONField("free_links", default=[], null=True, blank=True)
    creation_date           = models.DateTimeField(default=datetime.now)
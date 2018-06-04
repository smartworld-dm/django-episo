from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django.db import models
from jsonfield import JSONField
from datetime import datetime

class Brand(models.Model):
    user                    = models.OneToOneField(User, on_delete=models.CASCADE, default=0)
    name                    = models.CharField(max_length=50, null=True, blank=True)
    name_slug               = models.CharField(max_length=50, default="name_slug", null=True, blank=True)
    logo_image              = models.FileField(upload_to='uploads/', default="default.png", null=True, blank=True)
    cover_image             = models.FileField(upload_to='uploads/', default="default.png", null=True, blank=True)
    introduction            = models.TextField(default="", null=True, blank=True)
    small_introduction      = models.CharField(max_length=50, default="", null=True, blank=True)
    facebook_url            = models.CharField(max_length=200, default="https://facebook.com", null=True, blank=True)
    twitter_url             = models.CharField(max_length=200, default="https://twitter.com", null=True, blank=True)
    instagram_url           = models.CharField(max_length=200, default="https://instagram.com", null=True, blank=True)
    company_name            = models.CharField(max_length=200, default="company_name", null=True, blank=True)
    company_representative  = models.CharField(max_length=200, default="company_representative", null=True, blank=True)
    company_address         = models.CharField(max_length=200, default="company_address", null=True, blank=True)
    company_website         = models.CharField(max_length=200, default="company_website", null=True, blank=True)
    company_founding_date   = models.DateField(_("Date"), default=datetime.today)
    company_sales_offices   = models.TextField(default="sames_offices", null=True, blank=True)
    company_introduction    = models.TextField(default="company_introduction", null=True, blank=True)
    free_links              = JSONField("free_links", default={ "key": "value" }, null=True, blank=True)
    creation_date           = models.DateTimeField(default=datetime.now)
    
    def __str__(self):
        return self.name
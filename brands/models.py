from django.utils.translation import gettext as _
from django.db import models
from jsonfield import JSONField
import datetime

class Brand(models.Model):
    name                    = models.CharField(max_length=50)
    name_slug               = models.CharField(max_length=50, default="name_slug")
    introduction            = models.TextField(default="")
    small_introduction      = models.CharField(max_length=50, default="")
    logo_image              = models.FileField(default="default.png")
    cover_image             = models.FileField(default="default.png")
    facebook_url            = models.CharField(max_length=200, default="https://facebook.com", null=True, blank=True)
    twitter_url             = models.CharField(max_length=200, default="https://twitter.com", null=True, blank=True)
    instagram_url           = models.CharField(max_length=200, default="https://instagram.com", null=True, blank=True)
    company_name            = models.CharField(max_length=200, default="company_name")
    company_representative  = models.CharField(max_length=200, default="company_representative")
    company_address         = models.CharField(max_length=200, default="company_address")
    company_website         = models.CharField(max_length=200, default="company_website")
    company_founding_date   = models.DateField(_("Date"), default=datetime.date.today)
    company_sales_offices   = models.TextField(default="sames_offices")
    company_introduction    = models.TextField(default="company_introduction")
    free_links              = JSONField("free_links", default={'key':'value'})
    creation_date           = models.DateField(_("Date"), default=datetime.date.today)
    
    def __str__(self):
        return self.name
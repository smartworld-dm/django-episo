from django.db import models
from jsonfield import JSONField

# Create your models here.
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    # brand_id = 
    is_featured = models.BooleanField()
    cover_image = models.FileField()
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
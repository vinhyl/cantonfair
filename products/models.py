from django.db import models
from ckeditor.fields import RichTextField
from .storage import OverwriteStorage


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()

    def __unicode__(self):
        return self.name


class Product(models.Model):
    model = models.CharField(max_length=50)
    category = models.ForeignKey(Category)
    description = RichTextField()
    photo = models.ImageField(upload_to="photo", storage=OverwriteStorage())
    document = models.FileField(upload_to="document", storage=OverwriteStorage())
    order = models.IntegerField(default=100)

    class Meta:
        ordering = ["order"]

    def __unicode__(self):
        return self.model

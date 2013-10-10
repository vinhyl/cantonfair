from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Product(models.Model):
    model = models.CharField(max_length=50)
    category = models.ForeignKey(Category)
    description = models.TextField()
    photo = models.ImageField(upload_to="photo")
    document = models.FileField(upload_to="document")

    def __unicode__(self):
        return self.model

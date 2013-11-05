from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    website = models.URLField(blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50)
    address = models.TextField(blank=True)
    request = models.TextField(blank=True)

    def __unicode__(self):
        return self.name

from django.db import models
import urllib.request


# Create your models here.

class Link(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()

    @property
    def url_ok(self):
        try:
            return urllib.request.urlopen(self.url)
        except urllib.error.URLError:
            return "Invalid URL"

    def _unicode__(self):
        return self.title

r = "er"

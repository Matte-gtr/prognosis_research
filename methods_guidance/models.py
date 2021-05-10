from django.db import models


class Textbook(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    image = models.ImageField()
    image_link = models.URLField()
    description = models.CharField(max_length=1254, blank=False, null=False)
    optional_link = models.URLField(blank=True)
    optional_link_text = models.CharField(max_length=124, blank=True)

    def __str__(self):
        return self.name

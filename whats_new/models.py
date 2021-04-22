from django.db import models
from django.utils import timezone


class Latest_Research_Year(models.Model):
    year = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return str(self.year)


class Research_Update(models.Model):
    year = models.ForeignKey(Latest_Research_Year, on_delete=models.SET_NULL,
                             null=True)
    update = models.CharField(blank=False, null=False, max_length=254)
    link_url = models.URLField(blank=True, max_length=1024)
    link_name = models.CharField(blank=True, max_length=56)

    def __str__(self):
        return self.update


class Site_Page(models.Model):
    name = models.CharField(max_length=56, blank=False, null=False)
    page_link = models.CharField(max_length=254, blank=False, null=False)

    def __str__(self):
        return self.name


class Site_Log(models.Model):
    date = models.DateField(blank=False)
    updated_page = models.ForeignKey(Site_Page, on_delete=models.CASCADE)
    message_p1 = models.CharField(max_length=254, blank=False, null=False)
    link_1_url = models.URLField(blank=True)
    link_1_name = models.CharField(max_length=56, blank=True)
    message_p2 = models.CharField(max_length=254, blank=True)
    link_2_url = models.URLField(blank=True)
    link_2_name = models.CharField(max_length=56, blank=True)

    def __str__(self):
        return self.message_p1

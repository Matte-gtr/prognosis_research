from django.db import models
from django.utils import timezone


class Quote_of_note(models.Model):
    quote = models.CharField(max_length=500, null=False, blank=False)
    author = models.CharField(max_length=120, null=False, blank=False)
    comments = models.CharField(max_length=500, blank=True)
    date_added = models.DateField(blank=False, null=False)

    class Meta:
        verbose_name = 'Quote of note'
        verbose_name_plural = 'Quotes of note'

    def __str__(self):
        return self.quote

    def save(self, *args, **kwargs):
        if not self.pk:
            self.date_added = timezone.now()
        return super(Quote_of_note, self).save(*args, **kwargs)

from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True)
    author_first_name = models.CharField(max_length=256, null=True, blank=True)
    author_last_name = models.CharField(max_length=256, null=True, blank=True)
    publish = models.CharField(max_length=256, null=True, blank=True)

    class Meta:

        verbose_name_plural = "Books"




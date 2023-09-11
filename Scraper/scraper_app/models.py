from django.db import models


class Link(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=1000, null=True, blank=True)


    def __str__(self) -> str:
        return self.name
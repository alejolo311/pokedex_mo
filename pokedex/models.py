from django.db import models
from django.contrib.postgres.fields import ArrayField


class Pokemon(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=200)
    image = models.CharField(max_length=100)
    height = models.IntegerField()
    weight = models.IntegerField()
    stats = models.JSONField(blank=True, null=True)
    evolution = ArrayField(
        models.IntegerField(blank=True, null=True),
        size=8, blank=True, null=True
    )
    prevolution = models.IntegerField(blank=True, null=True)
    chain = models.IntegerField()

    def __str__(self):
        return str(self.name)

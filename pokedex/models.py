from django.db import models


class Pokemon(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=200)
    image = models.CharField(max_length=100)
    height = models.IntegerField()
    weight = models.IntegerField()
    stats = models.JSONField(blank=True, null=True)
    evolves_from = models.ForeignKey("self", blank=True, null=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.name)
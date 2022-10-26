from tabnanny import verbose
from django.db import models
from .event_entity import Event

class Image(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, null=False, editable=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField(max_length=300, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    categories = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return "Image: {}, {}, {}, {}".format( self.id, self.name, self.categories, self.created_at )

    class Meta:
        db_table = 'images'
        verbose_name = "Image"
        verbose_name_plural = "Images"
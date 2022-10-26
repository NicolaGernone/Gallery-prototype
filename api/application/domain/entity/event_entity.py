from django.db import models

class Event(models.Model):
    user_id = models.IntegerField(default=0, editable=True)
    image_id = models.UUIDField(primary_key=True, null=False, editable=False)
    view = models.IntegerField(default=0, editable=True)
    click = models.IntegerField(default=0, editable=True)
    weight = models.DecimalField(default=0.00, editable=True, max_digits=5, decimal_places=2)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return "Event: clicks {}, views {}, weight {}".format( self.click, self.view, self.weight )

    class Meta:
        db_table = 'events'
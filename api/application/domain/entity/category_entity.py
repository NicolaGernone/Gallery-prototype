from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return "Category: {}".format( self.name )

    class Meta:
        db_table = 'categories'
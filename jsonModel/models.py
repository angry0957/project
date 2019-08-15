from django.db import models
from django.contrib.postgres.fields import JSONField
from django.utils.timezone import now
# Create your models here.

class JsonModel(models.Model):
    name = models.CharField(max_length=200)
    data = JSONField()
    date = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        """A string representation of the model."""
        return self.name

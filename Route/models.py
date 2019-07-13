from django.db import models
from django.utils.timezone import now


class Route(models.Model):
    route = models.CharField(max_length=255, unique=True)

    def __str__(self):
        """A string representation of the model."""
        return self.route

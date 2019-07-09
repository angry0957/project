from django.db import models
from django.utils.timezone import now


class Route(models.Model):
    route = models.CharField(max_length=255)
    bill = models.IntegerField()
    exp = models.IntegerField()
    salary = models.IntegerField()
    petrol = models.IntegerField()
    income_tax = models.IntegerField()
    pra = models.IntegerField()
    total_expense = models.IntegerField()
    income = models.IntegerField()
    cheque = models.IntegerField()
    date = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        """A string representation of the model."""
        return self.route

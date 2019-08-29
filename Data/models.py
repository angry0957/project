from django.db import models
from django.utils.timezone import now
from Route.models import Route


class Data(models.Model):
    route = models.ForeignKey(Route, on_delete=models.DO_NOTHING)
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
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        """A string representation of the model."""
        return str(self.bill)

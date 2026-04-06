from django.db import models
from django.contrib.auth.models import User

class Expense(models.Model):

    TRANSACTION_TYPE = [
        ('income', 'Income'),
        ('expense', 'Expense'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=1000)
    amount = models.IntegerField(default=0)

    type = models.CharField(max_length=10, choices=TRANSACTION_TYPE)
    category = models.CharField(max_length=100)
    notes = models.TextField(blank=True, null=True)

    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.amount}"


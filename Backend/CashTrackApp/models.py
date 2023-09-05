from django.db import models

class Account(models.Model):
    accountNumber = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    # Add more fields as needed

    def __str__(self):
        return self.name+" "+self.accountNumber
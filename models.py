# payroll/models.py
from django.db import models
from django.contrib.auth.models import User
from employer.models import Employer

class Payroll(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Payroll for {self.user.username}"

  

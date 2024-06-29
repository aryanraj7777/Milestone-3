# payroll/tasks.py
from django_q.tasks import async_task
from .models import Payroll

@async_task
def calculate_payroll(payroll_id):
    payroll = Payroll.objects.get(id=payroll_id)
    # Calculate payroll logic goes here
    # ...
    payroll.save()

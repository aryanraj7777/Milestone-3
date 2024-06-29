# payroll/tasks.py (continued)
@async_task
def calculate_payroll(payroll_id):
    # ...
    payroll.save()
    send_payroll_email(payroll)

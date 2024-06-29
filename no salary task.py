# payroll/tasks.py (continued)
@async_task
def calculate_payroll(payroll_id):
    payroll = Payroll.objects.get(id=payroll_id)
    user = payroll.user
    if not payroll.salary:
        # Send an email or notification to the user/HR to update the salary
        print("User has no salary. Please update the salary.")
        return
    # ...

# payroll/tasks.py (continued)
@async_task
def calculate_payroll(payroll_id):
    payroll = Payroll.objects.get(id=payroll_id)
    user = payroll.user
    if not user.employer:
        # Send an email or notification to the user/HR to update the employer
        print("User has no employer. Please update the employer.")
        return
    # ...

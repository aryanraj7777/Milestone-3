# payroll/tasks.py (continued)
import datetime

@async_task
def schedule_payroll_calculations():
    today = datetime.date.today()
    if today.day == 1:  # Run on the 1st day of the month
        eligible_users = User.objects.filter(is_active=True, is_staff=False)  # assume is_active and is_staff fields in User model
        for user in eligible_users:
            payroll = Payroll.objects.get_or_create(user=user, employer=user.employer)[0]
            calculate_payroll.delay(p

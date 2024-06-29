# payroll/tasks.py (continued)
@async_task
def calculate_payroll(payroll_id):
    payroll = Payroll.objects.get(id=payroll_id)
    user = payroll.user
    employer = payroll.employer
    salary = payroll.salary

    # Calculate salary cuttings based on position
    salary_cuttings = SalaryCutting.objects.filter(position=user.position)
    total_cutting = 0
    for cutting in salary_cuttings:
        total_cutting += cutting.amount

    # Calculate additions (leaves) taken
    leaves_taken = user.leaves_taken  # assume leaves_taken is a field in User model

    # Calculate payroll
    net_salary = salary - total_cutting + leaves_taken
    payroll.net_salary = net_salary
    payroll.save()

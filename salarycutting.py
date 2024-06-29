# payroll/models.py (continued)
class SalaryCutting(models.Model):
    position = models.CharField(max_length=50)
    cutting_type = models.CharField(max_length=20)  # e.g., tax, insurance, etc.
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Salary Cutting for {self.position} - {self.cutting_type}"

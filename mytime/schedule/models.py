from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Supervisor(models.Model):
    department = models.OneToOneField(
        Department,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)
    


     
class Employee(models.Model):
    supervisor = models.ForeignKey(
        Supervisor,
        on_delete=models.CASCADE
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    work_from = models.DateField()
    def __str__(self):
        return '%s %s' % (self.first_name,self.last_name)

class WorkTime(models.Model):
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE
    )
    work_date = models.DateField()
    TIME_CHOICES = [
    ('Shift', (
            ('8', '8'),
            ('16', '16'),
        )
    ),
    ('Other', (
            ('l4', 'l4'),
            ('vacation', 'vacation'),
        )
    ),
    
    
    ]
    time = models.CharField(
        max_length=10,
        choices=TIME_CHOICES,
        default=8,
    )
    def __str__(self):
        return '%s %s -%s -%s' % (self.employee.first_name,self.employee.last_name, self.time, self.work_date)
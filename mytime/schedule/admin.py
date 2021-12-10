from django.contrib import admin
from .models import Department,Employee,Supervisor,WorkTime

admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Supervisor)
admin.site.register(WorkTime)
# Register your models here.

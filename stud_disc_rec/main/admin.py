from django.contrib import admin
from .models import Student,Incidents,Evidence,Notifications,Disciplinary_Actions,Records
# Register your models here.
admin.site.register(Student)
admin.site.register(Incidents)
admin.site.register(Evidence)
admin.site.register(Disciplinary_Actions)
admin.site.register(Records)
admin.site.register(Notifications)
from django.db import models

# Create your models here.

from django.db import models
from django.db import models

class Student(models.Model):
    Stud_ID = models.IntegerField(primary_key=True)
    FName = models.CharField(max_length=50)
    LName = models.CharField(max_length=50)
    Dept = models.CharField(max_length=45)
    Levl = models.IntegerField()
    Phone_No = models.CharField(max_length=11)
    Next_of_Kin = models.CharField(max_length=50)
    password=models.CharField(max_length=6)
    Next_of_Kin_Phone_No = models.CharField(max_length=11)

    def check_password(self, entered_password):

        return self.password == entered_password
   

class Incidents(models.Model):
    Incident_No = models.CharField(max_length=5, primary_key=True)
    Date_of_Occurence = models.DateField()
    Location = models.CharField(max_length=25)
    Descr = models.TextField()
    Stud_ID = models.ForeignKey(Student, on_delete=models.CASCADE)

class Evidence(models.Model):
    Evidence_No = models.CharField(max_length=5, primary_key=True)
    Ev_Type = models.CharField(max_length=30)
    Details = models.TextField()
    Incident_No = models.ForeignKey(Incidents, on_delete=models.CASCADE)
    Stud_ID = models.ForeignKey(Student, on_delete=models.CASCADE)

class Disciplinary_Actions(models.Model):
    Case_No = models.CharField(max_length=5, primary_key=True)
    Date_of_Hearing = models.DateField()
    Penance_Type = models.CharField(max_length=50)
    Penance_Details = models.TextField()
    Stud_ID = models.ForeignKey(Student, on_delete=models.CASCADE)
    Incident_No = models.ForeignKey(Incidents, on_delete=models.CASCADE)

class Records(models.Model):
    Record_No = models.CharField(max_length=5, primary_key=True)
    Case_Status = models.CharField(max_length=50)
    Stud_ID = models.ForeignKey(Student, on_delete=models.CASCADE)
    Incident_No = models.ForeignKey(Incidents, on_delete=models.CASCADE)
    Case_No = models.ForeignKey(Disciplinary_Actions, on_delete=models.CASCADE)


class Notifications(models.Model):
    Notification_ID = models.CharField(max_length=5, primary_key=True)
    Case_Subject = models.CharField(max_length=30)
    Details = models.TextField()
    Stud_ID = models.ForeignKey(Student, on_delete=models.CASCADE)
    Incident_No = models.ForeignKey(Incidents, on_delete=models.CASCADE)
    Case_No = models.ForeignKey(Disciplinary_Actions, on_delete=models.CASCADE)



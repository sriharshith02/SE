from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Details(models.Model):
    dept=models.CharField(max_length=5)
    course_name=models.CharField(max_length=100)
    duration=models.IntegerField()
    seats_available=models.IntegerField()
    fee=models.IntegerField(default=1000)

class Enrolled(models.Model):
    choicess=(
        ('CSE','CSE'),
        ('EEE','EEE'),
        ('IT','IT'),
        ('CIVIL','CIVIL'),
    )
    choicee=(
        ('CSE-Python','CSE-Python'),
        ('CSE-R and software Development','CSE-R and software Development'),
        ('CSE-Fundamentals of java programming','CSE-Fundamentals of java programming'),
        ('IT-Web Development or Full Stack Developer','IT-Web Development or Full Stack Developer'),
        ('IT-Google Cloud Platform Architecture','IT-Google Cloud Platform Architecture'),
        ('IT-JavaScript','IT-JavaScript'),
        ('EEE-Electrical Safety Course','EEE-Electrical Safety Course'),
        ('EEE-Equipment Selection Specialisation','EEE-Equipment Selection Specialisation'),
        ('EEE-Plant Earthing course','EEE-Plant Earthing course'),
        ('CIVIL-Bridge Engineering','CIVIL-Bridge Engineering'),
        ('CIVIL-Irrigation Engineering','CIVIL-Irrigation Engineering'),
        ('CIVIL-Hydraulic Engineering','CIVIL-Hydraulic Engineering'),
    )
    sno=models.AutoField(primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    department=models.CharField(max_length=5,choices=choicess,verbose_name='What is your department',default='CSE')
    c_name=models.CharField(max_length=100,choices=choicee,verbose_name='Which course do you want to take up?',default='Python')
class table(models.Model):
    name=models.CharField(max_length=50)
    course=models.TextField()


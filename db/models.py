from django.db import models
from django.contrib.auth.models import User

Departments = (
    ('CSE', 'Computer Science and Engineering'),
    ('ECE', 'Electronics and Communication Engineering'),
    ('EEE', 'Electrical and Electronics Engineering'),
    ('MECH', 'Mechanical Engineering'),
    ('CIVIL', 'Civil Engineering'),
    ('CSBS', 'Computer Science and Business Systems'),
    ('AIDS', 'Artificial Intelligence and Data Science'),
    ('CCE', 'Computer and Communication Engineering'),
    ('IT', 'Information Technology'),
)
# Create your models here.
class Department(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100,choices=Departments)

    def __str__(self):
        return self.department

class Certificate(models.Model):
    ID = models.CharField(max_length=100, unique=True, primary_key=True)
    Name = models.CharField(max_length=100)
    College = models.CharField(max_length=100)
    Event = models.CharField(max_length=100)
    Dept = models.CharField(max_length=100,choices=Departments)
    CreatedBy = models.ForeignKey(User, on_delete=models.CASCADE)
    Datetime = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.ID
    
class SymposiumInfo(models.Model):
    dept = models.CharField(max_length=100,choices=Departments, primary_key=True)
    dept_full_name = models.CharField(max_length=255)
    symp_name =  models.CharField(max_length=255)
    symp_date = models.DateField()
    convenor = models.CharField(max_length=255)

    def __str__(self):
        return self.symp_name
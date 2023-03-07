from django.db import models
from django.contrib.auth.models import User

Departments = (
    ('CSE', 'Computer Science and Engineering'),
    ('ECE', 'Electronics and Communication Engineering'),
    ('EEE', 'Electrical and Electronics Engineering'),
    ('ME', 'Mechanical Engineering'),
    ('CE', 'Civil Engineering'),
    ('CSBS', 'Computer Science and Business Systems'),
    ('MBA', 'Master of Business Administration'),
    ('AIDS', 'Artificial Intelligence and Data Science'),
    ('CCE', 'Computer Science and Communication Engineering'),
    ('IT', 'Information Technology'),
)
# Create your models here.
class Department(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100,choices=Departments)

class Certificate(models.Model):
    StudentName = models.CharField(max_length=100)
    StudentEmail = models.EmailField(max_length=100)
    StudentCollege = models.CharField(max_length=100)
    CreatedBy = models.ForeignKey(User, on_delete=models.CASCADE)
    Datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.StudentName
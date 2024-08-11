from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_principal = models.BooleanField('Is principal', default=False)
    is_teacher = models.BooleanField('Is teacher', default=False)
    is_student = models.BooleanField('Is student', default=False)


class Classroom(models.Model):
    name = models.CharField(max_length=255)
    start_time = models.TimeField()
    end_time = models.TimeField()
    active_days = models.CharField(max_length=255)  # e.g., 'Monday, Tuesday, Wednesday'

    def __str__(self):
        return self.name

class Timetable(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    start_time = models.TimeField()
    end_time = models.TimeField()
    days = models.CharField(max_length=255)  # e.g., 'Monday, Tuesday'

    def __str__(self):
        return f"{self.subject} in {self.classroom.name}"


from django.db import models
import uuid

class Student(models.Model):

    Gender_Choices = [
        ('M', 'Male'),
        ('F', 'Female')
    ]

    Academic_Level_Choices = [
        ('P.1', 'Primary 1'),
        ('P.2', 'Primary 2'),
        ('P.3', 'Primary 3'),
        ('P.4', 'Primary 4'),
        ('P.5', 'Primary 5'),
        ('P.6', 'Primary 6'),
        ('S.1', 'Secondary 1'),
        ('S.2', 'Secondary 2'),
        ('S.3', 'Secondary 3'),
        ('S.4', 'Secondary 4'),
        ('S.5', 'Secondary 5')
    ]

    Enrollment_Status_Choices = [
        ('Active', 'Active'),
        ('dismissed', 'Dismissed'),
        ('transferred', 'Transferred'),
        ('graduated', 'Graduated')
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField("Birth Date")
    gender = models.CharField(max_length=10, choices=Gender_Choices)
    current_academic_level = models.CharField('Current Academic Level', max_length=100, choices=Academic_Level_Choices)
    enrolment_status = models.CharField('Enrolment Status', max_length=100, choices=Enrollment_Status_Choices, default='Active')
    photo = models.ImageField(upload_to='students/photos', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
from django.db import models
# Create your models here.


class User(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=[(
        'male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    blood_group = models.CharField(max_length=5, choices=[
        ('A+', 'A+'), ('B+', 'B+'), ('O+', 'O+'),
        ('A-', 'A-'), ('B-', 'B-'), ('O-', 'O-'),
        ('AB+', 'AB+'), ('AB-', 'AB-')
    ],
        null=False,
        default='')
    address = models.TextField(max_length=300, null=True, default='')
    city = models.CharField(max_length=50, null=True, default='')
    state = models.CharField(max_length=50, null=True, default='')
    can_donate = models.BooleanField(null=True, default=False)
    mobile = models.CharField(null=True, default='', max_length=13)

    def name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.name()

# class Bank(models.Model):
#     name = models.CharField(max_length=100)
#     state = models.CharField(max_length=100)
#     city = models.CharField(max_length=100)
#     address = models.CharField(max_length=200)
#     mobile = models.CharField(max_length=15)
#     contactNo = models.CharField(max_length=20)

#     def __str(self):
#         return self.name()

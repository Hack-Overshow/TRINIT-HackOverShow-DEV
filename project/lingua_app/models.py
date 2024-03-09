

from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=[('student', 'Student'), ('tutor', 'Tutor')])
 

class Tutor(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    languages = models.CharField(max_length=100, blank=True)
    experience = models.IntegerField(null=True, blank=True)
    pricing = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
 

class Student(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    
    flashcards = models.ManyToManyField('Flashcard', blank=True, related_name='students_flashcards')
     

class TimeSlot(models.Model):
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

class Flashcard(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='flashcards_student')
    term = models.CharField(max_length=255)
    definition = models.TextField()

class Subscription(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    # env me keys dal dena

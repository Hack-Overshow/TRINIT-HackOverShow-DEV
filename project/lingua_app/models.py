from django.contrib.auth.models import User, AbstractUser, Group, Permission
from django.db import models
import uuid
from django.utils.text import slugify
import datetime


class Meeting(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)  # creator of the meeting
    title_of_meeting = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)  # the time meeting was created
    updated = models.DateTimeField(auto_now=True)  # time meeting was updated
    starting_date_time = models.DateTimeField()
    unique_meeting_name = models.TextField(blank=True, null=True)

    def __str__(self):
        return '%s: %s' % (self.creator, self.title_of_meeting)

    def save(self, *args, **kwargs):
        if not self.unique_meeting_name:
            self.unique_meeting_name = slugify(
                str(self.title_of_meeting) + '-' + str(uuid.uuid4())
            )
        return super(Meeting, self).save()

    @property
    def meeting_time(self):
        return (datetime.datetime.now() >= self.starting_date_time) and (
                datetime.datetime.now() <= self.ending_date_time
        )


class User(AbstractUser):
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)
    role = models.CharField(max_length=10, choices=[('student', 'Student'), ('tutor', 'Tutor')])

    # Define unique related_names for groups and user_permissions
    # to avoid clashes with the default auth User model
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text=(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name='lingua_user_groups',
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='lingua_user_permissions',
        related_query_name='user',
    )

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

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

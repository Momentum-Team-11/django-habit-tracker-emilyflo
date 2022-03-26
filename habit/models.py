from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Q

class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username} pk={self.pk}>"

    def __str__(self):
        return self.username

class HabitManager(models.Manager):
    def for_user(self, user):
        if user.is_authenticated:
            habits = self.filter(Q(public=True) | Q(author=user))
        else:
            habits = self.filter(public=True)
        return habits


class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='habits', default=True)
    name = models.CharField(max_length=150, blank=False)
    action = models.CharField(max_length=20, blank=False)
    target = models.IntegerField(blank=False)
    units = models.CharField(max_length=20, blank=False)
    start = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.name

class Record(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, related_name='habit')
    date = models.DateField(auto_now_add=True)
    record = models.IntegerField(blank=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['habit', 'record'], name='one_record_per_day')
        ]


    def __str__(self):
        return str(self.record)

    def __str__(self):
        return f"{self.date} {self.record}"
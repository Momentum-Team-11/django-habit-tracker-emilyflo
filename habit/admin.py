from django.contrib import admin
from .models import Habit, Record, User

admin.site.register(Habit)
admin.site.register(Record)
admin.site.register(User)

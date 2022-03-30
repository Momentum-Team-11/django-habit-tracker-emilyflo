from habit.models import Habit
from rest_framework import serializers


class HabitSerializer(serializers.ModelSerializer):
  class Meta:
    model = Habit
    fields = (
      "pk",
      "name",
      "action",
      "target",
      "units",
      "start",
    )
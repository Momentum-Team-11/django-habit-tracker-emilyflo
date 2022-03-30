from habit.models import Habit, Record
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

class RecordsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Record
    fields = (
      "pk",
      "habit",
      "date",
      "record",
      "units",
    )

class HabitRecordsSerializer(serializers.ModelSerializer):
  records = RecordsSerializer(many=True, required=False)
  class Meta:
    model = Habit
    fields = (
      "pk",
      "name",
      "records",
    )
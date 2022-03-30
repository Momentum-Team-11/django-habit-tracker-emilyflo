from rest_framework.views import APIView
from rest_framework.response import Response
from habit.models import Habit, Record
from .serializers import HabitSerializer, HabitRecordsSerializer, RecordsSerializer
from rest_framework.generics import ListCreateAPIView
from rest_framework.mixins import CreateModelMixin


class HabitListView(ListCreateAPIView):
  queryset = Habit.objects.all()
  serializer_class = HabitSerializer


class RecordsListView(ListCreateAPIView):
  queryset = Record.objects.all()
  serializer_class = RecordsSerializer
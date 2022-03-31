from rest_framework.views import APIView
from rest_framework.response import Response
from habit.models import Habit, Record, User
from .serializers import HabitSerializer, HabitRecordsSerializer, RecordsSerializer
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import CreateModelMixin


class HabitListView(ListAPIView):
  queryset = Habit.objects.all()
  serializer_class = HabitSerializer

class RecordsListView(ListCreateAPIView):
  queryset = Record.objects.all()
  serializer_class = RecordsSerializer

class HabitDetailsView(RetrieveUpdateDestroyAPIView):
  queryset = Habit.objects.all()
  serializer_class = HabitRecordsSerializer

# class UserList(ListAPIView):
#   queryset = User.objects.all()
#   serializer_class = UserSerializer
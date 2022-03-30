from rest_framework.views import APIView
from rest_framework.response import Response
from habit.models import Habit
from .serializers import HabitSerializer
from rest_framework.generics import ListAPIView
from rest_framework.mixins import CreateModelMixin

# just wanted to go through the process anyways
# class HabitListView(APIView):
#   def get(self, request, format=None):
#       """
#       List all the habits
#       """
#       habits = Habit.objects.all()
#       serializer = HabitSerializer(habits, many=True)
#       # return a response with json data
#       return Response(serializer.data)

#refactor views to use a Generic View
class HabitListView(ListAPIView):
  queryset = Habit.objects.all()
  serializer_class = HabitSerializer

# class AddHabitView(mixins.CreateModelMixin):
#   def create(self, request, *args, **kwargs):
#     serializer = self.get_serializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     self.perform_create(serializer)
#     headers = self.get_success_headers(serializer.data)
#     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
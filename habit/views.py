from django.shortcuts import render, redirect, get_object_or_404
from .models import Habit
from .forms import HabitForm, RecordForm
from django.contrib.auth.decorators import login_required

def splash(request):
  if request.user.is_authenticated:
    return redirect('index')
  return render(request, 'splash.html')

@login_required
def index(request):
  habits = Habit.objects.all()
  return render(request, 'index.html', {'habits': habits})

@login_required
def detail(request, pk):
  habit = get_object_or_404(Habit, pk=pk)
  form = HabitForm()
  return render(request, 'detail.html', {'habit': habit, 'form': form})
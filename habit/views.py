from django.shortcuts import render, redirect, get_object_or_404

import habit
from .models import Habit, Record
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
  records = Record.objects.all().filter(habit_id=habit.id)
  form = HabitForm()
  return render(request, 'detail.html', {'habit': habit, 'form': form, 'records': records})

@login_required
def add_habit(request):
  if request.method == 'GET':
    form = HabitForm()
  else:
    form = HabitForm(data=request.POST)
    if form.is_valid():
      form.save()
      return redirect(to='index')
  return render(request, 'add_habit.html', {'form': form})

@login_required
def add_record(request, habit_pk):
  habit = get_object_or_404(Habit, pk=habit_pk)
  if request.method == 'GET':
    form = RecordForm()
  else:
    form = RecordForm(data=request.POST)
    if form.is_valid():
      record = form.save(commit=False)
      record.habit = habit
      record.save()
      return redirect(to='detail', pk=habit.pk)

  return render(request, 'add_record.html', {'form': form, 'habit': habit})

@login_required
def edit_record(request, pk):
  records = get_object_or_404(Record, pk=pk)
  records = habit.record.all()
  if request.method == 'POST':
    form = RecordForm(request.POST, instance=record)
    if form.is_valid():
      record = form.save(commit=False)
      record.save()
      return redirect(to='detail', pk=pk)
  else:
    form = RecordForm(instance=record)

  return render(request, 'edit_record.html', {'form': form, 'record': record, 'records': records, 'habits': habits})
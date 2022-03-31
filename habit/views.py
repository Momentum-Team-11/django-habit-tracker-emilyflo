from django.shortcuts import render, redirect, get_object_or_404
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
      
@login_required
def edit_habit(request, pk):
  habit = get_object_or_404(Habit, pk=pk)
  if request.method == 'GET':
    form = HabitForm(instance=habit)
  else:
    form = HabitForm(data=request.POST, instance=habit)
    if form.is_valid():
      form.save()
      return redirect(to='detail', pk=habit.pk)
  return render(request, 'edit_habit.html', {'habit': habit, 'form': form})

@login_required
def delete_habit(request, pk):
  habit = get_object_or_404(Habit, pk=pk)
  if request.method == 'POST':
    habit.delete()
    return redirect(to='index')
  return render(request, 'delete_habit.html', {'habit': habit})

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
  record = Record.objects.filter(pk=pk).first()
  if request.method == 'GET':
    form = RecordForm(instance=record)
  else:
    form = RecordForm(request.POST, instance=record)
    if form.is_valid():
      form.save()
      return redirect(to='detail', pk=record.habit.pk)
  return render(request, 'edit_record.html', {'form': form, 'record': record})
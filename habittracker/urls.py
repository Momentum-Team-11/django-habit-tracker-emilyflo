"""habittracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from habit import views as habit_views
from api import views as api_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('', habit_views.splash, name='splash'),
    path('index', habit_views.index, name='index'),
    path('detail/<int:pk>/', habit_views.detail, name='detail'),
    path('add_habit/', habit_views.add_habit, name='add_habit'),
    path('habits/<int:pk>/edit/', habit_views.edit_habit, name='edit_habit'),
    path('habits/<int:pk>/delete/', habit_views.delete_habit, name='delete_habit'),
    path('habits/<int:habit_pk>/records', habit_views.add_record, name='add_record'),
    path('habits/<int:pk>/', habit_views.edit_record, name='edit_record'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/habit', api_views.HabitListView.as_view(), name='api_habit_list'),
    path('api/habits/records', api_views.RecordsListView.as_view(), name='api_records_list')
    # path('api/add_habit', api_views.AddHabitView.as_view(), name='api_add_habit'),
            ]
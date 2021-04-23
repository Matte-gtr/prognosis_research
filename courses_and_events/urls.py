from django.urls import path
from . import views


urlpatterns = [
    path('', views.courses_and_events, name="courses_and_events"),
    path('training_courses/', views.training_courses, name="training_courses"),
    path('conferences/', views.conferences, name="conferences"),
]

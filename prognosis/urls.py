from django.urls import path
from . import views


urlpatterns = [
    path('', views.prognosis, name="prognosis"),
    path('video_introduction/', views.video_introduction,
         name="video_introduction"),
    path('what_is_prognosis/', views.what_is_prognosis,
         name="what_is_prognosis"),
    path('what_is_prognosis_research/', views.what_is_prognosis_research,
         name="what_is_prognosis_research"),
    path('the_progress_framework/', views.the_progress_framework,
         name="the_progress_framework"),
    path('quotes_of_note/', views.quotes_of_note, name="quotes_of_note"),
]

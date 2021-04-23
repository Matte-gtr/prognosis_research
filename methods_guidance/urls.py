from django.urls import path
from . import views


urlpatterns = [
    path('', views.methods_guidance, name="methods_guidance"),
    path('progress_series/', views.progress_series,
         name="progress_series"),
    path('prognostic_factors/', views.prognostic_factors,
         name="prognostic_factors"),
    path('prognostic_models/', views.prognostic_models,
         name="prognostic_models"),
    path('systematic_reviews_and_meta_analysis/',
         views.systematic_reviews_and_meta_analysis,
         name="systematic_reviews_and_meta_analysis"),
    path('reporting/', views.reporting, name="reporting"),
    path('software_websites_and_apps/', views.software_websites_and_apps,
         name="software_websites_and_apps"),
    path('textbooks/', views.textbooks,
         name="textbooks"),
]

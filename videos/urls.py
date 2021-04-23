from django.urls import path
from . import views


urlpatterns = [
    path('', views.videos, name="videos"),
    path('controversies_in_prediction_modeling/',
         views.controversies_in_prediction_modeling,
         name="controversies_in_prediction_modeling"),
    path('covid19_prediction_models/', views.covid19_prediction_models,
         name="covid19_prediction_models"),
    path('emerging_topics_in_prediction_modeling/',
         views.emerging_topics_in_prediction_modeling,
         name="emerging_topics_in_prediction_modeling"),
    path('ipd_meta_analysis/', views.ipd_meta_analysis,
         name="ipd_meta_analysis"),
    path('penalisation_and_shrinkage/', views.penalisation_and_shrinkage,
         name="penalisation_and_shrinkage"),
    path('reporting_and_quality/', views.reporting_and_quality,
         name="reporting_and_quality"),
    path('sample_size_for_prediction_modeling/',
         views.sample_size_for_prediction_modeling,
         name="sample_size_for_prediction_modeling"),
    path('systematic_reviews/', views.systematic_reviews,
         name="systematic_reviews"),
]

from django.urls import path
from . import views


urlpatterns = [
    path('', views.whats_new, name="whats_new"),
    path('latest_research/', views.latest_research, name="latest_research"),
    path('site_updates_log', views.site_updates_log, name="site_updates_log"),
]

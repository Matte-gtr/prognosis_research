from django.urls import path
from . import views


urlpatterns = [
    path('', views.our_book, name="our_book"),
    path('scope_and_aims/', views.scope_and_aims,
         name="scope_and_aims"),
    path('table_of_contents/', views.table_of_contents,
         name="table_of_contents"),
    path('about_the_editors/', views.about_the_editors,
         name="about_the_editors"),
]

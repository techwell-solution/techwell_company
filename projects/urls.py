from django.urls import path
from . import views


urlpatterns = [
    path("solutions/", views.solutions, name="solutions"),
    path("projects/", views.projects, name="projects"),
    path("book/", views.booking, name="booking"),
    path("book/success/<int:booking_id>/", views.booking_success,  name="booking_success"),
    path("<slug:slug>/", views.project_detail, name="detail"),
]

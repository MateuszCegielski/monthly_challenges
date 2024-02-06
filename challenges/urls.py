from django.urls import path

from . import views

urlpatterns = [
    path("<int:month>", views.month_by_number_view),
    path("<str:month>", views.month_view, name="month-challenge"),
    path("", views.index, name="index")
]

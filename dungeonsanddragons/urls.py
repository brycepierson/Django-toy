from django.urls import path

from . import views

app_name = "dungeonsanddragons"
urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:monster_id>/", views.detail, name="detail"),
]
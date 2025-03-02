from django.urls import path
from . import views

app_name = "item"

urlpatterns = [
    path("", views.items, name="items"),
    path("new/", views.new, name="new"),
    path("new/toy/", views.new_toy, name="new_toy"),
    path("new/furniture/", views.new_furniture, name="new_furniture"),
    path("new/clothes/", views.new_clothes, name="new_clothes"),
    path("<int:pk>/", views.detail, name='detail'),
    path("<int:pk>/edit/", views.edit, name='edit'),
    path("<int:pk>/delete/", views.delete, name='delete'),
]

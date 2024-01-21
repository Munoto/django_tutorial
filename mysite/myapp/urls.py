from django.contrib import admin
from django.urls import path
from myapp.views import index, indexItem

urlpatterns = [
    path('', index),
    path('<int:my_id>/', indexItem, name = "detail"),
]
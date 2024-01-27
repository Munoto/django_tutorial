from django.contrib import admin
from django.urls import path
from myapp.views import index, indexItem, add_item

urlpatterns = [
    path('', index),
    path('<int:my_id>/', indexItem, name = "detail"),
    path('additem/', add_item, name = "add_item"),
]
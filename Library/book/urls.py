from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path
from book import views
app_name="book"

urlpatterns = [
    path('',views.home,name="home"),
    path('add',views.add,name="add"),
    path('add1',views.add1,name="add1"),
    path('fact', views.fact, name="fact"),
    path('view',views.view,name='view'),
    path('details/<int:p>', views.details, name='details'),
    path('edit/<int:p>', views.edit, name="edit"),
    path('delete/<int:p>', views.delete, name='delete'),
    path('search', views.search, name='search'),


]
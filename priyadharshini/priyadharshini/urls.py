from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [path('', views.calcs_Churn, name='calcs_Churn'),]
















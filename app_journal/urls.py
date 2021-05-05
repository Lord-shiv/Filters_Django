from django.urls import path
from . import views

app_name = 'app_journal'

urlpatterns = [
    path('', views.BootstrapFilterView, name='filter'),
]

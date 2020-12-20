from django.urls import path,include
from .views import ChartView

app_name = 'charts'

urlpatterns = [
    path('chartjs', ChartView.as_view(),name='chartjs'),
]
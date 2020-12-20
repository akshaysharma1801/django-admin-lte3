from django.urls import path
from .views import DashboardV1

app_name = 'dashboard'
urlpatterns = [
    path('v1', DashboardV1.as_view(),name='v1'),
]
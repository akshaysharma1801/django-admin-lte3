from django.urls import path
from .views import DashboardV1
from .views import DashboardV2
from .views import DashboardV3
from .views import Widgets


app_name = 'dashboard'
urlpatterns = [
    path('v1', DashboardV1.as_view(),name='v1'),
    path('v2', DashboardV2.as_view(),name='v2'),
    path('v3', DashboardV3.as_view(),name='v3'),
    path('widgets', Widgets.as_view(),name='widgets'),
]
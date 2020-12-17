from django.urls import path,include
from .views import RegisterView,LoginView

app_name = 'accounts'
urlpatterns = [
    path('', LoginView.as_view(),name='login'),
    path('register/', RegisterView.as_view(),name='register'),
]
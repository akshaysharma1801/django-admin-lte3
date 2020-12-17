from django.urls import path,include
from .views import RegisterView
from .views import LoginView
from .views import ForgotPasswordView


app_name = 'accounts'

urlpatterns = [
    path('', LoginView.as_view(),name='login'),
    path('register/', RegisterView.as_view(),name='register'),
    path('forgot-password/', ForgotPasswordView.as_view(),name='forgot-password'),
]
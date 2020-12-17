from django.shortcuts import render, redirect, reverse
from django.views import View

# Create your views here.
class LoginView(View):

    template_name = 'accounts/login.html'

    def get(self, request):
        return render(request, self.template_name)


class RegisterView(View):

    def get(self, request):
        pass

    def post(self, request):
        pass
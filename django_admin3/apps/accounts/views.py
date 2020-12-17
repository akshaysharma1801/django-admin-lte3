from django.shortcuts import render, redirect, reverse
from django.views import View


class LoginView(View):
    ''' User Login view. '''

    template_name = 'accounts/login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        pass    


class RegisterView(View):
    ''' User register view. '''

    template_name = 'accounts/register.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        pass

class ForgotPasswordView(View):
    ''' User forgot password view. '''

    template_name = 'accounts/forgot-password.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        pass
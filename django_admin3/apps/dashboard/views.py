from django.shortcuts import render, redirect, reverse
from django.views import View


class DashboardV1(View):
    ''' Dashboard v1 template. '''

    template_name = 'dashboard/index.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        pass    


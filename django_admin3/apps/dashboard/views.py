from django.shortcuts import render, redirect, reverse
from django.views import View


class DashboardV1(View):
    ''' Dashboard v1 template. '''

    template_name = 'dashboard/index.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        pass    


class DashboardV2(View):
    ''' Dashboard v2 template. '''

    template_name = 'dashboard/dashboard-v2.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        pass    


class DashboardV3(View):
    ''' Dashboard v3 template. '''

    template_name = 'dashboard/dashboard-v3.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        pass    


class Widgets(View):
    ''' Dashboard widgets template. '''

    template_name = 'dashboard/widgets.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        pass    



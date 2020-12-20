from django.shortcuts import render, redirect, reverse
from django.views import View


class ChartView(View):
    ''' Dashboard widgets template. '''

    template_name = 'chart/chartjs.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        pass    



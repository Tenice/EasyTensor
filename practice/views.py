from django.shortcuts import render
from rest_framework.decorators import detail_route
from rest_framework.viewsets import ViewSet

from practice.services import MNIST

APP_NAME_TO_CLASS = {
    'mnist': MNIST,
}

class PracticeViewSet(ViewSet):

    lookup_field = 'app_name'

    @detail_route(methods=['get'])
    def input_data(self, request, app_name=None):
        template_name = 'practice/data_input.html'
        return render(self.request, template_name)

    @detail_route(methods=['get'])
    def set_algorithm(self, request, app_name=None):
        template_name = 'practice/data_input.html'
        return render(self.request, template_name)

    @detail_route(methods=['get'])
    def set_training(self, request, app_name=None):
        template_name = 'practice/data_input.html'
        return render(self.request, template_name)

    @detail_route(methods=['get'])
    def run_test(self, request, app_name=None):
        template_name = 'practice/data_input.html'
        return render(self.request, template_name)

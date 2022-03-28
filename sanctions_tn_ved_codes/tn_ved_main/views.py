from django.views.generic import CreateView, ListView, FormView
from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from .models import *


def index(request):
    param_for_render = {
        'header_phones': "header_phones",
        'title': 'Проверка кодов ТН ВЭД'
    }
    return render(request, 'tn_ved_main/index.html', context=param_for_render)

# def show_search_results(request):
#
#     param_for_render = {
#
#         'title': 'Результаты поиска'
#     }
#     return render(request, 'tn_ved_main/search_results.html', context=param_for_render)


class SearchResultsView(ListView):
    model = ActualSanctionsTnvedCodes
    template_name = 'search_results.html'

    def get_queryset(self):  # новый
        query = self.request.GET.get('q')
        object_list = ActualSanctionsTnvedCodes.objects.filter(sanctions_tn_ved_code=query)
        return object_list


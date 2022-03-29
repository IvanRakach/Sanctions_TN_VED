from django.views.generic import CreateView, ListView, FormView, TemplateView
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

# class HomePageView(TemplateView):
#     template_name = 'home.html'

# def show_search_results(request):
#     query = SanctionsTnvedCodes.objects.filter()
#     param_for_render = {
#
#         'title': 'Результаты поиска'
#     }
#     return render(request, 'tn_ved_main/search_results.html', context=param_for_render)


class SearchResultsView(ListView):
    model = SanctionsTnvedCodes  # !!!!!!!!!!!!!!!!!!!!!!
    template_name = 'sanctionstnvedcodes_list.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = SanctionsTnvedCodes.objects.filter(sanctions_tn_ved_code=query)

        # query_2 = self.request.GET.get('q')
        # object_list_2 = SanctionsTnvedCodes.objects.filter(sanctions_tn_ved_code=query_2)

        return object_list


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

    # def get_queryset(self):
    #     query = self.request.GET.get('q')
    #     object_list = SanctionsTnvedCodes.objects.filter(sanctions_tn_ved_code=query)
    #     return object_list

    def get_queryset(self):  # новый
        query = self.request.GET.get('q')
        return SanctionsTnvedCodes.objects.filter(
            # для определения рус символов их нужно преобразовать в единый формат
            Q(sanctions_tn_ved_code__icontains=query) | Q(sanctions_tn_ved_code_description_rus__icontains=query) |
            Q(sanctions_tn_ved_code_description_eng__icontains=query)
            # Q(sanctions_tn_ved_code_description_rus__contains=query)
        )


def show_usa_sanctions_list(request):
    us_sanctions_query = SanctionsTnvedCodes.objects.filter(country_code_2_dig_1side__contains="US")
    # us_sanctions_query = SanctionsTnvedCodes.objects.filter(sanctions_tn_ved_code__contains="7225")
    param_for_render = {
        'us_sanctions_query': us_sanctions_query,
    }
    return render(request, 'tn_ved_main/USA_sanctions_list.html', context=param_for_render)

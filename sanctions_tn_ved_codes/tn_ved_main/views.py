from django.views.generic import CreateView, ListView, FormView, TemplateView
from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from .models import *

# карта
# from django.shortcuts import render, redirect  # , render_to_response
from django.http import HttpResponse
from django.template.loader import get_template
from django.template.context import RequestContext
import pandas as pd
import folium
# import geopandas

# url = 'https://en.wikipedia.org/wiki/List_of_countries_by_meat_consumption'
# tables = pd.read_html(url)
# table = tables[0]

# pd.set_option('display.max_columns', 10)
# pd.set_option('display.width', 1000)
# pd.set_option('display.max_rows', 200)

# def folium_map(request):
#     coords = [(40.7831, -73.9712), (40.6782, -73.9412), (40.7282, -73.7949)]
#     map = folium.Map(location=[40.7118, -74.0131], zoom_start=12)
#     for coord in coords:
#         folium.Marker(location=[coord[0], coord[1]]).add_to(map)
#     context = {'map': map}
#     return render(request, 'tn_ved_main/template.html', context)







# конец карты

def index(request):
    param_for_render = {
        'title': 'Проверка кодов ТН ВЭД',
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
    #     object_list = SanctionsTnvedCodes.objects.filter(
    #             Q(sanctions_tn_ved_code__icontains=query) | Q(sanctions_tn_ved_code_description_rus__icontains=query) |
    #             Q(sanctions_tn_ved_code_description_eng__icontains=query))
    #
    #     return object_list

    def get_queryset(self):  # рабочий вариант
        query = self.request.GET.get('q')
        return SanctionsTnvedCodes.objects.filter(
            # для определения рус символов их нужно преобразовать в единый формат
            Q(sanctions_tn_ved_code__icontains=query) | Q(sanctions_tn_ved_code_description_rus__icontains=query) |
            Q(sanctions_tn_ved_code_description_eng__icontains=query)
            # Q(sanctions_tn_ved_code_description_rus__contains=query)
        )

##############################################################################################
# -------------------------------------- Другие страны ------------------------------------- #
##############################################################################################


def show_usa_sanctions_list(request):
    us_sanctions_query = SanctionsTnvedCodes.objects.filter(country_code_2_dig_1side__icontains="US")
    # us_sanctions_query = SanctionsTnvedCodes.objects.filter(sanctions_tn_ved_code__contains="7225")
    param_for_render = {
        'us_sanctions_query': us_sanctions_query,
        'title': 'Список санкционных кодов США',
    }
    return render(request, 'tn_ved_main/USA_sanctions_list.html', context=param_for_render)


def show_uk_sanctions_list(request):
    uk_sanctions_query = SanctionsTnvedCodes.objects.filter(country_code_2_dig_1side__icontains="UK")
    param_for_render = {
        'uk_sanctions_query': uk_sanctions_query,
        'title': 'Список санкционных кодов Великоритании',
    }
    return render(request, 'tn_ved_main/UK_sanctions_list.html', context=param_for_render)


def show_eu_sanctions_list(request):
    eu_sanctions_query = SanctionsTnvedCodes.objects.filter(country_code_2_dig_1side__icontains="EU")
    param_for_render = {
        'eu_sanctions_query': eu_sanctions_query,
        'title': 'Список санкционных кодов ЕС',
    }
    return render(request, 'tn_ved_main/EU_sanctions_list.html', context=param_for_render)


def show_jp_sanctions_list(request):
    jp_sanctions_query = SanctionsTnvedCodes.objects.filter(country_code_2_dig_1side__icontains="JP")
    param_for_render = {
        'jp_sanctions_query': jp_sanctions_query,
        'title': 'Список санкционных кодов Японии',
    }
    return render(request, 'tn_ved_main/JP_sanctions_list.html', context=param_for_render)


def show_ch_sanctions_list(request):
    ch_sanctions_query = SanctionsTnvedCodes.objects.filter(country_code_2_dig_1side__icontains="CH")
    param_for_render = {
        'ch_sanctions_query': ch_sanctions_query,
        'title': 'Список санкционных кодов Швейцарии',
    }
    return render(request, 'tn_ved_main/CH_sanctions_list.html', context=param_for_render)


def show_ca_sanctions_list(request):
    ca_sanctions_query = SanctionsTnvedCodes.objects.filter(country_code_2_dig_1side__icontains="CA")
    param_for_render = {
        'ca_sanctions_query': ca_sanctions_query,
        'title': 'Список санкционных кодов Канады',
    }
    return render(request, 'tn_ved_main/CA_sanctions_list.html', context=param_for_render)


def show_au_sanctions_list(request):
    au_sanctions_query = SanctionsTnvedCodes.objects.filter(country_code_2_dig_1side__icontains="AU")
    param_for_render = {
        'au_sanctions_query': au_sanctions_query,
        'title': 'Список санкционных кодов Австралии',
    }
    return render(request, 'tn_ved_main/AU_sanctions_list.html', context=param_for_render)

##############################################################################################
# -------------------------------- Итого по "другим странам" ------------------------------- #
##############################################################################################


def show_all_other_sanctions_list(request):
    all_other_sanctions_query = SanctionsTnvedCodes.objects.filter(
        Q(country_code_2_dig_1side__icontains="US") | Q(country_code_2_dig_1side__icontains="UK") |
        Q(country_code_2_dig_1side__icontains="EU") | Q(country_code_2_dig_1side__icontains="JP") |
        Q(country_code_2_dig_1side__icontains="CH") | Q(country_code_2_dig_1side__icontains="CA") |
        Q(country_code_2_dig_1side__icontains="AU")
    )
    param_for_render = {
        'all_other_sanctions_query': all_other_sanctions_query,
        'title': 'Список санкционных кодов стран Запада',
    }
    return render(request, 'tn_ved_main/ALL_OTHER_sanctions_query_sanctions_list.html', context=param_for_render)

##############################################################################################
# ------------------------------------------- РФ ------------------------------------------- #
##############################################################################################


def show_ru_311_sanctions_list(request):
    ru_311_sanctions_query = SanctionsTnvedCodes.objects.filter(country_code_2_dig_1side__icontains="RU-311")
    param_for_render = {
        'ru_311_sanctions_query': ru_311_sanctions_query,
        'title': 'Список санкционных кодов РФ (Постановление №311)',
    }
    return render(request, 'tn_ved_main/RU_311_sanctions_list.html', context=param_for_render)


def show_ru_312_sanctions_list(request):
    ru_312_sanctions_query = SanctionsTnvedCodes.objects.filter(country_code_2_dig_1side__icontains="RU-312")
    param_for_render = {
        'ru_312_sanctions_query': ru_312_sanctions_query,
        'title': 'Список санкционных кодов РФ (Постановление №312)',
    }
    return render(request, 'tn_ved_main/RU_312_sanctions_list.html', context=param_for_render)


def show_ru_313_sanctions_list(request):
    ru_313_sanctions_query = SanctionsTnvedCodes.objects.filter(country_code_2_dig_1side__icontains="RU-313")
    param_for_render = {
        'ru_313_sanctions_query': ru_313_sanctions_query,
        'title': 'Список санкционных кодов РФ (Постановление №313)',
    }
    return render(request, 'tn_ved_main/RU_313_sanctions_list.html', context=param_for_render)

##############################################################################################
# ------------------------------------------- РБ ------------------------------------------- #
##############################################################################################


def show_by_147_sanctions_list(request):
    by_147_sanctions_query = SanctionsTnvedCodes.objects.filter(country_code_2_dig_1side__icontains="BY-147")
    param_for_render = {
        'by_147_sanctions_query': by_147_sanctions_query,
        'title': 'Список санкционных кодов РБ (Постановление №147)',
    }
    return render(request, 'tn_ved_main/BY_147_sanctions_list.html', context=param_for_render)


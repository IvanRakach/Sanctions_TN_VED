from django.views import View
# from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from .models import *


def index(request):
    param_for_render = {
        'title': 'Проверка кодов ТН ВЭД',
    }
    return render(request, 'tn_ved_main/index.html', context=param_for_render)


class SearchResultsView(View):
    template_name = 'tn_ved_main/sanctionstnvedcodes_list.html'

    def get(self, request, *args, **kwargs):
        param_for_render = {}

        q = request.GET.get('q')
        if q is not None:
            query_sets_1 = SanctionsTnvedCodes.objects.search(query=q)
            query_sets_2 = SanctionsTnvedCodesFromRU311312313BY147.objects.search(query=q)

            param_for_render = {
                # 'final_query': final_query,
                'query_sets_1': query_sets_1,
                'query_sets_2': query_sets_2
            }

        return render(request=request, template_name=self.template_name, context=param_for_render)

##############################################################################################
# -------------------------------------- Другие страны ------------------------------------- #
##############################################################################################


def show_usa_sanctions_list(request):
    us_sanctions_query = SanctionsTnvedCodes.objects.filter(sanctions_initiator_country_code_2_dig__icontains="US")
    param_for_render = {
        'us_sanctions_query': us_sanctions_query,
        'title': 'Список санкционных кодов США',
    }
    return render(request, 'tn_ved_main/USA_sanctions_list.html', context=param_for_render)


def show_uk_sanctions_list(request):
    uk_sanctions_query = SanctionsTnvedCodes.objects.filter(sanctions_initiator_country_code_2_dig__icontains="GB")
    param_for_render = {
        'uk_sanctions_query': uk_sanctions_query,
        'title': 'Список санкционных кодов Великоритании',
    }
    return render(request, 'tn_ved_main/UK_sanctions_list.html', context=param_for_render)


def show_eu_sanctions_list(request):
    eu_sanctions_query = SanctionsTnvedCodes.objects.filter(sanctions_initiator_country_code_2_dig__icontains="EU")
    param_for_render = {
        'eu_sanctions_query': eu_sanctions_query,
        'title': 'Список санкционных кодов ЕС',
    }
    return render(request, 'tn_ved_main/EU_sanctions_list.html', context=param_for_render)


def show_jp_sanctions_list(request):
    jp_sanctions_query = SanctionsTnvedCodes.objects.filter(sanctions_initiator_country_code_2_dig__icontains="JP")
    param_for_render = {
        'jp_sanctions_query': jp_sanctions_query,
        'title': 'Список санкционных кодов Японии',
    }
    return render(request, 'tn_ved_main/JP_sanctions_list.html', context=param_for_render)


def show_ch_sanctions_list(request):
    ch_sanctions_query = SanctionsTnvedCodes.objects.filter(sanctions_initiator_country_code_2_dig__icontains="CH")
    param_for_render = {
        'ch_sanctions_query': ch_sanctions_query,
        'title': 'Список санкционных кодов Швейцарии',
    }
    return render(request, 'tn_ved_main/CH_sanctions_list.html', context=param_for_render)


def show_ca_sanctions_list(request):
    ca_sanctions_query = SanctionsTnvedCodes.objects.filter(sanctions_initiator_country_code_2_dig__icontains="CA")
    param_for_render = {
        'ca_sanctions_query': ca_sanctions_query,
        'title': 'Список санкционных кодов Канады',
    }
    return render(request, 'tn_ved_main/CA_sanctions_list.html', context=param_for_render)


def show_au_sanctions_list(request):
    au_sanctions_query = SanctionsTnvedCodes.objects.filter(sanctions_initiator_country_code_2_dig__icontains="AU")
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
        Q(sanctions_initiator_country_code_2_dig__icontains="US") |
        Q(sanctions_initiator_country_code_2_dig__icontains="GB") |
        Q(sanctions_initiator_country_code_2_dig__icontains="EU") |
        Q(sanctions_initiator_country_code_2_dig__icontains="JP") |
        Q(sanctions_initiator_country_code_2_dig__icontains="CH") |
        Q(sanctions_initiator_country_code_2_dig__icontains="CA") |
        Q(sanctions_initiator_country_code_2_dig__icontains="AU")
    )
    param_for_render = {
        'all_other_sanctions_query': all_other_sanctions_query,
        'title': 'Список санкционных кодов стран "Западного мира"',
    }
    return render(request, 'tn_ved_main/ALL_OTHER_sanctions_query_sanctions_list.html', context=param_for_render)

##############################################################################################
# ------------------------------------------- РФ ------------------------------------------- #
##############################################################################################


def show_ru_311_sanctions_list(request):
    ru_311_sanctions_query = SanctionsTnvedCodesFromRU311312313BY147.objects.filter(
        sanction_country_iso_alpha_2__icontains="RU",
        doc_number__icontains="311",
    )
    param_for_render = {
        'ru_311_sanctions_query': ru_311_sanctions_query,
        'title': 'Список санкционных кодов РФ (Постановление №311)',
    }
    return render(request, 'tn_ved_main/RU_311_sanctions_list.html', context=param_for_render)


def show_ru_312_sanctions_list(request):
    ru_312_sanctions_query = SanctionsTnvedCodesFromRU311312313BY147.objects.filter(
        sanction_country_iso_alpha_2__icontains="RU",
        doc_number__icontains="312",
    )
    param_for_render = {
        'ru_312_sanctions_query': ru_312_sanctions_query,
        'title': 'Список санкционных кодов РФ (Постановление №312)',
    }
    return render(request, 'tn_ved_main/RU_312_sanctions_list.html', context=param_for_render)


def show_ru_313_sanctions_list(request):
    ru_313_sanctions_query = SanctionsTnvedCodesFromRU311312313BY147.objects.filter(
        sanction_country_iso_alpha_2__icontains="RU",
        doc_number__icontains="313",
    )
    param_for_render = {
        'ru_313_sanctions_query': ru_313_sanctions_query,
        'title': 'Список санкционных кодов РФ (Постановление №313)',
    }
    return render(request, 'tn_ved_main/RU_313_sanctions_list.html', context=param_for_render)


def show_list_of_restricted_countries_ru(request):
    list_of_restricted_countries_ru = SanctionCountriesListFromRU313.objects.all()
    param_for_render = {
        'list_of_restricted_countries_ru': list_of_restricted_countries_ru,
    }
    return render(request, 'tn_ved_main/list_of_restricted_countries_ru.html', context=param_for_render)
##############################################################################################
# ------------------------------------------- РБ ------------------------------------------- #
##############################################################################################


def show_by_147_sanctions_list(request):
    by_147_sanctions_query = SanctionsTnvedCodesFromRU311312313BY147.objects.filter(
        sanction_country_iso_alpha_2__icontains="BY",
        doc_number__icontains="147",
    )
    param_for_render = {
        'by_147_sanctions_query': by_147_sanctions_query,
        'title': 'Список санкционных кодов РБ (Постановление №147)',
    }
    return render(request, 'tn_ved_main/BY_147_sanctions_list.html', context=param_for_render)


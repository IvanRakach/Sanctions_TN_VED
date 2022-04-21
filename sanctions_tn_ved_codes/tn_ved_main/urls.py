from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.index, name="home"),
    path('search_results/', SearchResultsView.as_view(), name='search_results'),
    path('usa_sanctions_list/', views.show_usa_sanctions_list, name='usa_sanctions_list'),
    path('uk_sanctions_list/', views.show_uk_sanctions_list, name='uk_sanctions_list'),
    path('eu_sanctions_list/', views.show_eu_sanctions_list, name='eu_sanctions_list'),
    path('jp_sanctions_list/', views.show_jp_sanctions_list, name='jp_sanctions_list'),
    path('ch_sanctions_list/', views.show_ch_sanctions_list, name='ch_sanctions_list'),
    path('ca_sanctions_list/', views.show_ca_sanctions_list, name='ca_sanctions_list'),
    path('au_sanctions_list/', views.show_au_sanctions_list, name='au_sanctions_list'),
    path('all_other_sanctions_list/', views.show_all_other_sanctions_list, name='all_other_sanctions_list'),
    path('ru_311_sanctions_list/', views.show_ru_311_sanctions_list, name='ru_311_sanctions_list'),
    path('ru_312_sanctions_list/', views.show_ru_312_sanctions_list, name='ru_312_sanctions_list'),
    path('ru_313_sanctions_list/', views.show_ru_313_sanctions_list, name='ru_313_sanctions_list'),
    path('list_of_restricted_countries_ru/', views.show_list_of_restricted_countries_ru,
         name='list_of_restricted_countries_ru'),
    path('by_147_sanctions_list/', views.show_by_147_sanctions_list, name='by_147_sanctions_list'),
]

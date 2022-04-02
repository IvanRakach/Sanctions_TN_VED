from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.index, name="home"),
    path('search_results/', SearchResultsView.as_view(), name='search_results'),
    # path('search_results/', views.show_search_results, name='search_results'),
    path('usa_sanctions_list', views.show_usa_sanctions_list, name='usa_sanctions_list')
]

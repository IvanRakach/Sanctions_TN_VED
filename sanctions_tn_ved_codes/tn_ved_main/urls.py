from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.index, name="home"),
    path('search_results/', SearchResultsView.as_view(), name='search_results'),
    # path('search/', views.show_search_results, name='search_results'),
]

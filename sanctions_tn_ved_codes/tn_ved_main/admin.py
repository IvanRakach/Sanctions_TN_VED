from django.contrib import admin

# Register your models here.

from .models import *
# from .forms import *


class ActualTnvedDirectoryAdmin(admin.ModelAdmin):
    # список полей, которые мы хотим видеть в нашей админ панели
    list_display = ('id', 'tn_ved_code', 'tn_ved_code_description', )
    # те поля, на которые мы можем кликнуть и перейти
    list_display_links = ('id', 'tn_ved_code')
    # те поля, по которым мы можем производить поиск информации
    search_fields = ('tn_ved_code', 'tn_ved_code_description', )


admin.site.register(ActualTnvedDirectory, ActualTnvedDirectoryAdmin)


class ActualSanctionsTnvedCodesAdmin(admin.ModelAdmin):
    # список полей, которые мы хотим видеть в нашей админ панели
    list_display = ('id', 'sanctions_tn_ved_code', 'sanctions_tn_ved_code_description', 'country_code_2_dig', )
    # те поля, на которые мы можем кликнуть и перейти
    list_display_links = ('id', 'sanctions_tn_ved_code')
    # те поля, по которым мы можем производить поиск информации
    search_fields = ('sanctions_tn_ved_code', 'sanctions_tn_ved_code_description', )


admin.site.register(ActualSanctionsTnvedCodes, ActualSanctionsTnvedCodesAdmin)


class CountriesAgainstRFRBAdmin(admin.ModelAdmin):
    # список полей, которые мы хотим видеть в нашей админ панели
    list_display = ('id', 'country_code_2_dig', )
    # те поля, на которые мы можем кликнуть и перейти
    list_display_links = ('id', 'country_code_2_dig')
    # те поля, по которым мы можем производить поиск информации
    search_fields = ('country_code_2_dig', )


admin.site.register(CountriesAgainstRFRB, CountriesAgainstRFRBAdmin)


class ResultTableAdmin(admin.ModelAdmin):
    # список полей, которые мы хотим видеть в нашей админ панели
    list_display = ('id', 'tn_ved_code', 'sanctions_tn_ved_code', 'country_code_2_dig', )
    # те поля, на которые мы можем кликнуть и перейти
    list_display_links = ('id', 'tn_ved_code')
    # те поля, по которым мы можем производить поиск информации
    search_fields = ('tn_ved_code', 'sanctions_tn_ved_code', 'country_code_2_dig', )


admin.site.register(ResultTable, ResultTableAdmin)

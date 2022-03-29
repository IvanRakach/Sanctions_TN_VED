from django.contrib import admin

# Register your models here.

from .models import *
# from .forms import *


class SanctionsTnvedCodesAdmin(admin.ModelAdmin):
    # список полей, которые мы хотим видеть в нашей админ панели
    list_display = (
        'id',
        'sanctions_tn_ved_code',
        'sanctions_tn_ved_code_description_eng',
        'sanctions_tn_ved_code_description_rus',
        'country_code_2_dig_1side',
        'country_code_2_dig_2side',
    )
    # те поля, на которые мы можем кликнуть и перейти
    list_display_links = ('id', 'sanctions_tn_ved_code', )
    # те поля, по которым мы можем производить поиск информации
    search_fields = (
        'sanctions_tn_ved_code',
        'sanctions_tn_ved_code_description_eng',
        'sanctions_tn_ved_code_description_rus',
        'country_code_2_dig_1side',
        'country_code_2_dig_2side',
    )


admin.site.register(SanctionsTnvedCodes, SanctionsTnvedCodesAdmin)


class TnVedCodesAdmin(admin.ModelAdmin):
    # список полей, которые мы хотим видеть в нашей админ панели
    list_display = ('id', 'tn_ved_code', )
    # те поля, на которые мы можем кликнуть и перейти
    list_display_links = ('id', 'tn_ved_code',)
    # те поля, по которым мы можем производить поиск информации
    search_fields = ('tn_ved_code', )


admin.site.register(TnVedCodes, TnVedCodesAdmin)

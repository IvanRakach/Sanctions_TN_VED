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
        'type_of_restrictions',
        'country_code_2_dig_1side',
        'country_code_2_dig_2side',
        'sanctions_initiator_country_code_2_dig',
        'export_import_ru',
        'note',
    )
    # те поля, на которые мы можем кликнуть и перейти
    list_display_links = ('id', 'sanctions_tn_ved_code', )
    # те поля, по которым мы можем производить поиск информации
    search_fields = (
        'sanctions_tn_ved_code',
        'sanctions_tn_ved_code_description_eng',
        'sanctions_tn_ved_code_description_rus',
        'type_of_restrictions',
        'country_code_2_dig_1side',
        'country_code_2_dig_2side',
        'sanctions_initiator_country_code_2_dig',
        'export_import_ru',
        'note',
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


class SanctionsTnvedCodesFromRU311312313BY147Admin(admin.ModelAdmin):
    # список полей, которые мы хотим видеть в нашей админ панели
    list_display = (
        'id',
        'sanctions_tn_ved_code',
        'sanctions_tn_ved_code_description',
        'type_of_restrictions',
        'doc_name',
        'doc_number',
        'sanction_country_iso_alpha_2',
        'sanction_country_iso_alpha_3',
        'note',
    )
    # те поля, на которые мы можем кликнуть и перейти
    list_display_links = ('id', 'sanctions_tn_ved_code', )
    # те поля, по которым мы можем производить поиск информации
    search_fields = (
        'sanctions_tn_ved_code',
        'sanctions_tn_ved_code_description',
        'type_of_restrictions',
        'doc_name',
        'doc_number',
        'sanction_country_iso_alpha_2',
        'sanction_country_iso_alpha_3',
        'note',
    )


admin.site.register(SanctionsTnvedCodesFromRU311312313BY147, SanctionsTnvedCodesFromRU311312313BY147Admin)


class SanctionCountriesListFromRU313Admin(admin.ModelAdmin):
    # список полей, которые мы хотим видеть в нашей админ панели
    list_display = (
        'id',
        'sanction_country_rus',
        'sanction_country_iso_alpha_2',
        'sanction_country_iso_alpha_3',
        'eu_member_country',
        'type_of_restrictions',
        'doc_name',
        'doc_number',
        'note',
    )
    # те поля, на которые мы можем кликнуть и перейти
    list_display_links = ('id', 'sanction_country_rus', )
    # те поля, по которым мы можем производить поиск информации
    search_fields = (
        'sanction_country_rus',
        'sanction_country_iso_alpha_2',
        'sanction_country_iso_alpha_3',
        'eu_member_country',
        'type_of_restrictions',
        'doc_name',
        'doc_number',
        'note',
    )


admin.site.register(SanctionCountriesListFromRU313, SanctionCountriesListFromRU313Admin)

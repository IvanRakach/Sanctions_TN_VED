from django.contrib import admin
from .models import *


class SanctionsTnvedCodesAdmin(admin.ModelAdmin):
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
    list_display_links = ('id', 'sanctions_tn_ved_code', )
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
    list_display = ('id', 'tn_ved_code', )
    list_display_links = ('id', 'tn_ved_code',)
    search_fields = ('tn_ved_code', )


admin.site.register(TnVedCodes, TnVedCodesAdmin)


class SanctionsTnvedCodesFromRU311312313BY147Admin(admin.ModelAdmin):
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
    list_display_links = ('id', 'sanctions_tn_ved_code', )
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
    list_display_links = ('id', 'sanction_country_rus', )
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

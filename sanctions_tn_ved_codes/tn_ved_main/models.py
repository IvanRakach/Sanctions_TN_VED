from django.db import models
from django.db.models import Q


class SanctionsTnvedCodesQuerySet(models.QuerySet):
    def search(self, query=None):
        qs = self
        if query is not None:
            or_lookup = (Q(sanctions_tn_ved_code__icontains=query) |
                         Q(sanctions_tn_ved_code_description_eng__icontains=query) |
                         Q(sanctions_tn_ved_code_description_rus__icontains=query) |
                         Q(sanctions_initiator_country_code_2_dig__icontains=query)
                         )
            qs = qs.filter(or_lookup).distinct()

        return qs


class SanctionsTnvedCodesManager(models.Manager):
    def get_queryset(self):
        return SanctionsTnvedCodesQuerySet(self.model, using=self._db)

    def search(self, query=None):
        return self.get_queryset().search(query=query)


class SanctionsTnvedCodes(models.Model):
    sanctions_tn_ved_code = models.CharField('CN код', max_length=1500, db_index=True)
    sanctions_tn_ved_code_description_eng = models.TextField('Описание санкционного кода', )
    sanctions_tn_ved_code_description_rus = models.TextField('Описание санкционного кода (рус.)', )
    type_of_restrictions = models.TextField('Дополнительное пояснение', )
    country_code_2_dig_1side = models.CharField('Страна отправления', max_length=6)
    country_code_2_dig_2side = models.CharField('Страна назначения', max_length=6)
    sanctions_initiator_country_code_2_dig = models.CharField('Страна, которая ввела санкции', max_length=2)
    export_import_ru = models.CharField('Экспорт в РФ / Импорт в РФ', max_length=250)
    note = models.TextField('Примечание', default="-")

    objects = SanctionsTnvedCodesManager()

    def __str__(self):
        return self.sanctions_tn_ved_code

    class Meta:
        verbose_name = 'Список санкционных кодов стран "Западного мира"'
        verbose_name_plural = 'Список санкционных кодов стран "Западного мира"'


class TnVedCodes(models.Model):
    tn_ved_code = models.CharField('Номер кода ТН ВЭД', max_length=15)
    tn_ved_code_description = models.TextField('Описание кода ТН ВЭД', blank=True, default='Description', )

    def __str__(self):
        return self.tn_ved_code

    class Meta:
        verbose_name = 'Справочник кодов ТН ВЭД'
        verbose_name_plural = 'Справочник кодов ТН ВЭД'


class SanctionsTnvedCodesFromRU311312313BY147QuerySet(models.QuerySet):
    def search(self, query=None):
        qs = self
        if query is not None:
            or_lookup = (Q(sanctions_tn_ved_code__icontains=query) |
                         Q(sanctions_tn_ved_code_description__icontains=query) |
                         Q(sanction_country_iso_alpha_2__icontains=query)
                         )
            qs = qs.filter(or_lookup).distinct()

        return qs


class SanctionsTnvedCodesFromRU311312313BY147Manager(models.Manager):
    def get_queryset(self):
        return SanctionsTnvedCodesFromRU311312313BY147QuerySet(self.model, using=self._db)

    def search(self, query=None):
        return self.get_queryset().search(query=query)


class SanctionsTnvedCodesFromRU311312313BY147(models.Model):
    sanctions_tn_ved_code = models.CharField('Код ТН ВЭД ЕАЭС', max_length=250, db_index=True)
    sanctions_tn_ved_code_description = models.TextField('Описание кода', )
    type_of_restrictions = models.TextField('Вид ограничений', )
    doc_name = models.TextField('Наименование документа', )
    doc_number = models.IntegerField('Номер документа')
    sanction_country_iso_alpha_2 = models.CharField('Alpha-2 ISO 3166-1', max_length=2, db_index=True)
    sanction_country_iso_alpha_3 = models.CharField('Alpha-3 ISO 3166-1', max_length=3, db_index=True)
    note = models.TextField('Примечание', default="-")

    objects = SanctionsTnvedCodesFromRU311312313BY147Manager()

    def __str__(self):
        return self.sanctions_tn_ved_code


class SanctionCountriesListFromRU313(models.Model):
    sanction_country_rus = models.CharField('Наименование страны', max_length=200)
    sanction_country_iso_alpha_2 = models.CharField('Alpha-2 ISO 3166-1', max_length=2, db_index=True)
    sanction_country_iso_alpha_3 = models.CharField('Alpha-3 ISO 3166-1', max_length=3, db_index=True)
    eu_member_country = models.CharField('Страна-член ЕС', max_length=2)
    type_of_restrictions = models.TextField('Вид ограничения', )
    doc_name = models.TextField('Наименование документа', )
    doc_number = models.IntegerField('Номер документа')
    note = models.TextField('Примечание', default="-")

    def __str__(self):
        return self.sanction_country_rus

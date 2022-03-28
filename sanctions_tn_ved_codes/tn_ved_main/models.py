from django.db import models


class ActualTnvedDirectory(models.Model):
    tn_ved_code = models.CharField('Номер кода', max_length=15)
    tn_ved_code_description = models.TextField('Описание кода', blank=True, default='Description',)

    def __str__(self):
        return str(self.tn_ved_code)

    class Meta:
        verbose_name = 'Справочник кодов ТН ВЭД'
        verbose_name_plural = 'Справочник кодов ТН ВЭД'


class ActualSanctionsTnvedCodes(models.Model):
    sanctions_tn_ved_code = models.CharField('Номер санкционного кода', max_length=15)
    sanctions_tn_ved_code_description = models.TextField('Описание санкционного кода',
                                                         blank=True, default='Description')
    country_code_2_dig = models.ForeignKey('CountriesAgainstRFRB', null=True, on_delete=models.CASCADE,
                                           verbose_name="Код страны (2 символа)")

    def __str__(self):
        return str(self.sanctions_tn_ved_code)

    class Meta:
        verbose_name = 'Справочник санкционных кодов ТН ВЭД'
        verbose_name_plural = 'Справочник санкционных кодов ТН ВЭД'


class CountriesAgainstRFRB(models.Model):
    country_code_2_dig = models.CharField('Код страны (2 символа)', max_length=15)

    # magic method - возвращает имя категории
    def __str__(self):
        return self.country_code_2_dig

    # def get_absolute_url(self):
    #     return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Наименование страны'
        verbose_name_plural = 'Наименование стран'


class ResultTable(models.Model):
    tn_ved_code = models.ForeignKey('ActualTnvedDirectory', null=True, on_delete=models.CASCADE,
                                    verbose_name="Код ТН ВЭД")
    # tn_ved_code_description = models.ForeignKey('ActualTnvedDirectory', null=True, on_delete=models.CASCADE,
    #                                             verbose_name="Описание кода ТН ВЭД")
    sanctions_tn_ved_code = models.ForeignKey('ActualSanctionsTnvedCodes', null=True, on_delete=models.CASCADE,
                                              verbose_name="Санкционный код ТН ВЭД")
    country_code_2_dig = models.ForeignKey('CountriesAgainstRFRB', null=True, on_delete=models.CASCADE,
                                           verbose_name="Страна, которая ввела санкции")

    class Meta:
        verbose_name = 'Итоговая таблица'
        verbose_name_plural = 'Итоговая таблица'

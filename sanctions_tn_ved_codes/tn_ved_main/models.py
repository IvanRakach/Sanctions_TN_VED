# from audioop import reverse
from django.db import models


class SanctionsTnvedCodes(models.Model):
    sanctions_tn_ved_code = models.CharField('Номер санкционного кода', max_length=10, db_index=True)
    sanctions_tn_ved_code_description_eng = models.TextField('Описание санкционного кода',
                                                             default='Description_eng')
    sanctions_tn_ved_code_description_rus = models.TextField('Описание санкционного кода',
                                                             default='Description_rus')
    country_code_2_dig_1side = models.CharField('Буквенный код страны, которая ввела санкции', max_length=2)
    country_code_2_dig_2side = models.CharField('Буквенный код страны против которой ввели санкции', max_length=2)

    def __str__(self):
        return self.sanctions_tn_ved_code

    # def get_absolute_url(self):
    #     return reverse('category', kwargs={'cat _id': self.pk})

    class Meta:
        verbose_name = 'Список санкционных кодов ТН ВЭД'
        verbose_name_plural = 'Список санкционных кодов ТН ВЭД'


class TnVedCodes(models.Model):
    tn_ved_code = models.CharField('Номер кода ТН ВЭД', max_length=15)
    tn_ved_code_description = models.TextField('Описание кода ТН ВЭД', blank=True, default='Description', )
    # sanctions_tn_ved_code = models.ForeignKey('SanctionsTnvedCodes', on_delete=models.CASCADE)
    # sanctions_tn_ved_code_description = models.ForeignKey('SanctionsTnvedCodes', on_delete=models.CASCADE)
    # country_code_2_dig = models.ForeignKey('SanctionsTnvedCodes', on_delete=models.CASCADE)

    def __str__(self):
        return self.tn_ved_code

    class Meta:
        verbose_name = 'Справочник кодов ТН ВЭД'
        verbose_name_plural = 'Справочник кодов ТН ВЭД'

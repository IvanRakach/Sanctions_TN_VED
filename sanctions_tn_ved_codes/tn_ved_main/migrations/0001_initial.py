# Generated by Django 4.0.3 on 2022-04-21 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SanctionCountriesListFromRU313',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sanction_country_rus', models.CharField(max_length=20, verbose_name='Наименование страны')),
                ('sanction_country_iso_alpha_2', models.CharField(db_index=True, max_length=2, verbose_name='Alpha-2 ISO 3166-1')),
                ('sanction_country_iso_alpha_3', models.CharField(db_index=True, max_length=3, verbose_name='Alpha-3 ISO 3166-1')),
                ('eu_member_country', models.CharField(max_length=2, verbose_name='Страна-член ЕС')),
                ('type_of_restrictions', models.TextField(verbose_name='Вид ограничения')),
                ('doc_name', models.TextField(verbose_name='Наименование документа')),
                ('doc_number', models.IntegerField(verbose_name='Номер документа')),
                ('note', models.TextField(default='-', verbose_name='Примечание')),
            ],
        ),
        migrations.CreateModel(
            name='SanctionsTnvedCodes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sanctions_tn_ved_code', models.CharField(db_index=True, max_length=200, verbose_name='CN код')),
                ('sanctions_tn_ved_code_description_eng', models.TextField(verbose_name='Описание санкционного кода')),
                ('sanctions_tn_ved_code_description_rus', models.TextField(verbose_name='Описание санкционного кода (рус.)')),
                ('type_of_restrictions', models.TextField(verbose_name='Дополнительное пояснение')),
                ('country_code_2_dig_1side', models.CharField(max_length=2, verbose_name='Страна отправления')),
                ('country_code_2_dig_2side', models.CharField(max_length=2, verbose_name='Страна назначения')),
                ('sanctions_initiator_country_code_2_dig', models.CharField(max_length=2, verbose_name='Страна, которая ввела санкции')),
                ('export_import_ru', models.CharField(max_length=12, verbose_name='Экспорт в РФ / Импорт в РФ')),
                ('note', models.TextField(default='-', verbose_name='Примечание')),
            ],
            options={
                'verbose_name': 'Список санкционных кодов стран "Западного мира"',
                'verbose_name_plural': 'Список санкционных Стран "Западного мира"',
            },
        ),
        migrations.CreateModel(
            name='SanctionsTnvedCodesFromRU311312313BY147',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sanctions_tn_ved_code', models.CharField(db_index=True, max_length=10, verbose_name='Код ТН ВЭД ЕАЭС')),
                ('sanctions_tn_ved_code_description', models.TextField(verbose_name='Описание кода')),
                ('type_of_restrictions', models.TextField(verbose_name='Вид ограничений')),
                ('doc_name', models.TextField(verbose_name='Наименование документа')),
                ('doc_number', models.IntegerField(verbose_name='Номер документа')),
                ('sanction_country_iso_alpha_2', models.CharField(db_index=True, max_length=2, verbose_name='Alpha-2 ISO 3166-1')),
                ('sanction_country_iso_alpha_3', models.CharField(db_index=True, max_length=3, verbose_name='Alpha-3 ISO 3166-1')),
                ('note', models.TextField(default='-', verbose_name='Примечание')),
            ],
        ),
        migrations.CreateModel(
            name='TnVedCodes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tn_ved_code', models.CharField(max_length=15, verbose_name='Номер кода ТН ВЭД')),
                ('tn_ved_code_description', models.TextField(blank=True, default='Description', verbose_name='Описание кода ТН ВЭД')),
            ],
            options={
                'verbose_name': 'Справочник кодов ТН ВЭД',
                'verbose_name_plural': 'Справочник кодов ТН ВЭД',
            },
        ),
    ]

# Generated by Django 3.2.9 on 2022-05-26 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tn_ved_main', '0006_auto_20220526_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sanctioncountrieslistfromru313',
            name='sanction_country_rus',
            field=models.CharField(max_length=200, verbose_name='Наименование страны'),
        ),
    ]

# Generated by Django 3.2.9 on 2022-05-26 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tn_ved_main', '0003_alter_sanctionstnvedcodes_export_import_ru'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sanctionstnvedcodes',
            name='sanctions_tn_ved_code',
            field=models.CharField(db_index=True, max_length=1000, verbose_name='CN код'),
        ),
    ]

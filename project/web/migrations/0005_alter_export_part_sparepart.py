# Generated by Django 4.0 on 2022-01-30 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_bill_id_bill_alter_export_bill_id_bill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='export_part',
            name='sparepart',
            field=models.CharField(max_length=40),
        ),
    ]
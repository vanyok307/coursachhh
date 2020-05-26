# Generated by Django 3.0.5 on 2020-04-17 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('railway', '0008_auto_20200417_0137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='place_type',
            field=models.CharField(choices=[('Зг', 'Загальний'), ('Пк', 'Плацкартний'), ('Кп', 'Купейний'), ('Св', 'СВ'), ('Лк', 'Люкс')], max_length=20, verbose_name='Тип вагону'),
        ),
    ]

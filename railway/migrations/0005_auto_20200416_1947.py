# Generated by Django 3.0.5 on 2020-04-16 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('railway', '0004_auto_20200416_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='carriage',
            field=models.DateTimeField(default=None, verbose_name='Номер вагону'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='first',
            field=models.DateTimeField(default=None, verbose_name='дата прибуття'),
        ),
    ]

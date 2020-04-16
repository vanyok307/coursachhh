# Generated by Django 3.0.5 on 2020-04-16 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('railway', '0002_auto_20200416_1932'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='type_of_ticket',
            field=models.CharField(default=None, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ticket',
            name='number_of_place',
            field=models.IntegerField(default=None, verbose_name='Номер місця'),
        ),
    ]
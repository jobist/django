# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_products'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name_plural': 'Товары', 'verbose_name': 'Товар'},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Название категории', db_index=True, unique=True),
        ),
        migrations.AlterModelTable(
            name='category',
            table='category',
        ),
    ]

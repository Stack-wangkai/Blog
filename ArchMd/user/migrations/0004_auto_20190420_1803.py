# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-04-20 18:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20190420_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.PositiveIntegerField(choices=[(1, '正常'), (0, '删除'), (2, '草稿')], default=1, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.PositiveIntegerField(choices=[(1, 'Linux'), (2, 'Python'), (3, '数据库'), (4, '数据结构')], verbose_name='分类'),
        ),
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.BooleanField(default=1, verbose_name='正常'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='status',
            field=models.BooleanField(default=1, verbose_name='正常'),
        ),
    ]
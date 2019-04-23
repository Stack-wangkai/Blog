# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-04-20 17:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20190420_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.PositiveIntegerField(choices=[(1, '正常'), (0, '删除'), (2, '草稿')], verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.PositiveIntegerField(choices=[(1, 'Linux'), (2, 'Python'), (3, '数据库'), (4, '数据结构')], max_length=32, verbose_name='分类'),
        ),
    ]
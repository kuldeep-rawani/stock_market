# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2019-03-04 12:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('stock_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, max_length=255, primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('sell', 'sell'), ('buy', 'Buy')], max_length=255, verbose_name='Stock Buy')),
                ('amount', models.CharField(max_length=255, verbose_name='Stock Buy')),
                ('is_done', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='buy_stock', to='stock_app.User')),
            ],
        ),
        migrations.CreateModel(
            name='StockAllocation',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, max_length=255, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('buy_stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buy_stock_allocation', to='stock_app.Order')),
                ('sell_stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sell_stock_allocation', to='stock_app.Order')),
            ],
        ),
    ]

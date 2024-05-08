# Generated by Django 5.0.4 on 2024-05-08 20:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
        ('products', '0004_remove_product_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_published', models.DateTimeField(auto_now_add=True)),
                ('Product_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('client_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.clients')),
            ],
        ),
    ]

# Generated by Django 4.0.6 on 2022-09-02 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_sold_product_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sold_product_table',
            name='date_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

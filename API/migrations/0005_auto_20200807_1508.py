# Generated by Django 3.0.8 on 2020-08-07 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0004_auto_20200807_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csv_product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
    ]
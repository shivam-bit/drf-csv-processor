# Generated by Django 3.0.8 on 2020-08-07 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0003_file_uploads'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csv_product',
            name='price',
            field=models.FloatField(),
        ),
    ]

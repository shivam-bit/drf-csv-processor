# Generated by Django 3.0.8 on 2020-08-07 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0006_auto_20200807_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csv_product',
            name='customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='API.customer'),
        ),
        migrations.AlterUniqueTogether(
            name='csv_product',
            unique_together={('customer_id', 'title', 'price')},
        ),
    ]
# Generated by Django 4.2.16 on 2024-11-06 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furniture', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='furnitureitem',
            name='condition',
            field=models.CharField(default='Good', max_length=255),
        ),
        migrations.AddField(
            model_name='furnitureitem',
            name='rental_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]

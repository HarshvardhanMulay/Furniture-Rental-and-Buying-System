# Generated by Django 4.2.16 on 2024-10-28 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FurnitureItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('available_for_rent', models.BooleanField(default=False)),
                ('available_for_sale', models.BooleanField(default=True)),
            ],
        ),
    ]

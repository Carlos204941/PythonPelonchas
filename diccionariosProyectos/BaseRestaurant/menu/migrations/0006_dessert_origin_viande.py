# Generated by Django 4.1 on 2022-09-03 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_platmenuenfant_prixmenuenfant'),
    ]

    operations = [
        migrations.AddField(
            model_name='dessert',
            name='origin_viande',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]

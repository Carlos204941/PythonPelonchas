# Generated by Django 4.1 on 2022-09-03 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_rename_desserts_dessert_rename_plats_plat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entree',
            name='origin_viande',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='plat',
            name='origin_viande',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]

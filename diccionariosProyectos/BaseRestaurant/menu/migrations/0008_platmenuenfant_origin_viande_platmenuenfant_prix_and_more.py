# Generated by Django 4.1 on 2022-09-05 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0007_rename_nom_platmenuenfant_nom_et_ou_prix_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='platmenuenfant',
            name='origin_viande',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='platmenuenfant',
            name='prix',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='prixmenuenfant',
            name='origin_viande',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='prixmenuenfant',
            name='prix',
            field=models.FloatField(default=0),
        ),
    ]

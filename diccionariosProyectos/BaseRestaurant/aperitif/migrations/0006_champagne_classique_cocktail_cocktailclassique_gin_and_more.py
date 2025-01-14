# Generated by Django 4.1 on 2022-09-06 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aperitif', '0005_tapa_delete_tapas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Champagne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prix', models.FloatField(default=0)),
                ('ingredient', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Classique',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prix', models.FloatField(default=0)),
                ('ingredient', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Cocktail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prix', models.FloatField(default=0)),
                ('ingredient', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CocktailClassique',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prix', models.FloatField(default=0)),
                ('ingredient', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Gin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prix', models.FloatField(default=0)),
                ('ingredient', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SansAlcools',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prix', models.FloatField(default=0)),
                ('ingredient', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Vodka',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prix', models.FloatField(default=0)),
                ('ingredient', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Whiskie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prix', models.FloatField(default=0)),
                ('ingredient', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

# Generated by Django 4.1 on 2022-09-03 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_suggestion_plat_dessert_commentaire_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlatMenuEnfant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PrixMenuEnfant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PrixUnique', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]

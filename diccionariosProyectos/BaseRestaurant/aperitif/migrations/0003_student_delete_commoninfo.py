# Generated by Django 4.1 on 2022-09-06 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aperitif', '0002_commoninfo_delete_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prix', models.FloatField(default=0)),
                ('ingredient', models.CharField(blank=True, max_length=200)),
                ('home_group', models.CharField(max_length=5)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='CommonInfo',
        ),
    ]
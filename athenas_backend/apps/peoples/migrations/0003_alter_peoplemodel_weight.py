# Generated by Django 5.0 on 2023-12-08 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peoples', '0002_alter_peoplemodel_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peoplemodel',
            name='weight',
            field=models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Peso'),
        ),
    ]

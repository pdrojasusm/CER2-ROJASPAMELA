# Generated by Django 4.1.2 on 2022-11-13 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='correspondencia',
            name='f_entrega',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
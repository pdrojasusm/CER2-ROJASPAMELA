# Generated by Django 4.1.2 on 2022-11-13 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0006_alter_correspondencia_conserje_ent_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='correspondencia',
            name='conserje_ent',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]

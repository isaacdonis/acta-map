# Generated by Django 4.1 on 2023-10-17 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_subwaystations_equipmentno_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subwaystations',
            name='equipmentno',
            field=models.CharField(default='No information available', max_length=700),
        ),
        migrations.AlterField(
            model_name='subwaystations',
            name='shortdescription',
            field=models.CharField(default='No information available', max_length=700),
        ),
    ]
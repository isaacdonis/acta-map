# Generated by Django 4.1 on 2023-11-16 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_remove_subwaystations_equipmentno_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='subwaystations',
            name='all_comm_feedback',
            field=models.TextField(default='\n'),
        ),
    ]

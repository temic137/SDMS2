# Generated by Django 4.2.3 on 2023-11-09 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_incidents_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incidents',
            name='Location',
            field=models.CharField(max_length=25),
        ),
    ]

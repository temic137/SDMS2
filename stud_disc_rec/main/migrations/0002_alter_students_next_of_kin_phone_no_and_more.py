# Generated by Django 4.2.3 on 2023-11-09 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='Next_of_Kin_Phone_No',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='students',
            name='Phone_No',
            field=models.CharField(max_length=11),
        ),
    ]

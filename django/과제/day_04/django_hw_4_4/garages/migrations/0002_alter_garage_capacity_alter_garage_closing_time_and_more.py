# Generated by Django 4.2.11 on 2024-03-28 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='garage',
            name='capacity',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='garage',
            name='closing_time',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='garage',
            name='is_parking_avaliable',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='garage',
            name='location',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='garage',
            name='opening_time',
            field=models.TimeField(null=True),
        ),
    ]

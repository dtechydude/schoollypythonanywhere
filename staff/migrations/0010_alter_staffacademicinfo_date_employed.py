# Generated by Django 3.2 on 2022-03-30 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0009_auto_20220330_0414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffacademicinfo',
            name='date_employed',
            field=models.CharField(blank=True, default='000000', max_length=150),
        ),
    ]

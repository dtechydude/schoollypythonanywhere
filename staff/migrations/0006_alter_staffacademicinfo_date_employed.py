# Generated by Django 3.2 on 2022-03-16 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0005_auto_20220222_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffacademicinfo',
            name='date_employed',
            field=models.DateTimeField(null=True),
        ),
    ]
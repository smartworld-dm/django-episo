# Generated by Django 2.0.5 on 2018-06-01 22:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0003_auto_20180601_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='company_founding_date',
            field=models.DateField(default=datetime.datetime.today, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='cover_image',
            field=models.FileField(blank=True, default='default.png', null=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='brand',
            name='logo_image',
            field=models.FileField(blank=True, default='default.png', null=True, upload_to='uploads/'),
        ),
    ]

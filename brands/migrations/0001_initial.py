# Generated by Django 2.0.5 on 2018-06-03 02:06

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('name_slug', models.CharField(default='name_slug', max_length=50)),
                ('logo_image', models.FileField(blank=True, default='default.png', null=True, upload_to='uploads/')),
                ('cover_image', models.FileField(blank=True, default='default.png', null=True, upload_to='uploads/')),
                ('introduction', models.TextField(blank=True, default='', null=True)),
                ('small_introduction', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('facebook_url', models.CharField(blank=True, default='https://facebook.com', max_length=200, null=True)),
                ('twitter_url', models.CharField(blank=True, default='https://twitter.com', max_length=200, null=True)),
                ('instagram_url', models.CharField(blank=True, default='https://instagram.com', max_length=200, null=True)),
                ('company_name', models.CharField(blank=True, default='company_name', max_length=200, null=True)),
                ('company_representative', models.CharField(blank=True, default='company_representative', max_length=200, null=True)),
                ('company_address', models.CharField(blank=True, default='company_address', max_length=200, null=True)),
                ('company_website', models.CharField(blank=True, default='company_website', max_length=200, null=True)),
                ('company_founding_date', models.DateField(default=datetime.datetime.today, verbose_name='Date')),
                ('company_sales_offices', models.TextField(blank=True, default='sames_offices', null=True)),
                ('company_introduction', models.TextField(blank=True, default='company_introduction', null=True)),
                ('free_links', jsonfield.fields.JSONField(blank=True, default={'key': 'value'}, null=True, verbose_name='free_links')),
                ('creation_date', models.DateTimeField(default=datetime.datetime.now)),
                ('user', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

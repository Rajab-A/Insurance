# Generated by Django 4.2.5 on 2023-09-27 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service_provider',
            name='birth_date',
        ),
    ]

# Generated by Django 4.2.5 on 2023-09-27 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service_provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('service', models.CharField(max_length=20)),
                ('contact', models.CharField(max_length=10)),
                ('location', models.CharField(max_length=20)),
                ('birth_date', models.DateField()),
            ],
        ),
    ]


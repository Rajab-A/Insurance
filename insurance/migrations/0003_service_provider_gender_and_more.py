# Generated by Django 4.2.5 on 2023-09-27 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0002_remove_service_provider_birth_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='service_provider',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default=0, max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='service_provider',
            name='location',
            field=models.CharField(blank=True, default='N/A', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='service_provider',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Provider Name'),
        ),
    ]
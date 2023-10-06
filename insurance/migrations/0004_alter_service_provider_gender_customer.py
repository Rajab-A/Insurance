# Generated by Django 4.2.5 on 2023-09-27 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0003_service_provider_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service_provider',
            name='gender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male')], max_length=2),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('contact', models.CharField(max_length=10)),
                ('service_date', models.DateField()),
                ('service_recieved', models.BooleanField(default=False)),
                ('Service_Provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insurance.service_provider')),
            ],
        ),
    ]
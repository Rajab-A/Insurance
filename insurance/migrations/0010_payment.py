# Generated by Django 4.2.5 on 2023-10-04 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0009_customer_policy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateField()),
            ],
        ),
    ]

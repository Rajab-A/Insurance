# Generated by Django 4.2.5 on 2023-09-29 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0004_alter_service_provider_gender_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='contact',
            new_name='customer_contact',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='name',
            new_name='customer_name',
        ),
    ]

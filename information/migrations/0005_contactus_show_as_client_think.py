# Generated by Django 4.2.4 on 2023-08-29 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0004_aboutus_description_alter_aboutus_eita_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='show_as_client_think',
            field=models.BooleanField(default=False, verbose_name='show_as_client_think'),
        ),
    ]

# Generated by Django 4.2.4 on 2023-08-30 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0006_why_choose_us'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=100, verbose_name='question')),
                ('answer', models.TextField(verbose_name='answer')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
            ],
            options={
                'verbose_name': 'FAQ',
                'verbose_name_plural': 'FAQs',
            },
        ),
    ]
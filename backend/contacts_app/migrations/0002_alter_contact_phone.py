# Generated by Django 4.1.7 on 2023-03-17 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(default='xxx-xxx-xxxx', max_length=12),
        ),
    ]

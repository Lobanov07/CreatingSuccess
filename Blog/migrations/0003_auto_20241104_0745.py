# Generated by Django 3.2.16 on 2024-11-04 04:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='location',
        ),
        migrations.DeleteModel(
            name='Location',
        ),
    ]
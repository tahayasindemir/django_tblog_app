# Generated by Django 3.1.4 on 2021-01-09 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_auto_20210109_1656'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-created_date']},
        ),
    ]
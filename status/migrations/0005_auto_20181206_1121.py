# Generated by Django 2.1.2 on 2018-12-06 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0004_auto_20181118_2000'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='statuscomment',
            options={'ordering': ['-created_time']},
        ),
    ]

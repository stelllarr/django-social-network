# Generated by Django 2.1.2 on 2018-11-03 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]

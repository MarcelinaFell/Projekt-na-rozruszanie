# Generated by Django 3.0.2 on 2020-12-14 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('randomizer1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='randomizer1',
            name='summary',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
    ]

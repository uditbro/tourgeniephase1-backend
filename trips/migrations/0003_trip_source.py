# Generated by Django 5.1.7 on 2025-04-11 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='source',
            field=models.CharField(default='delhi', max_length=255),
        ),
    ]

# Generated by Django 5.1.5 on 2025-01-18 17:06

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_neighborhood_average_houses_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='change_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

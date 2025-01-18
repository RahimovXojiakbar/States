# Generated by Django 5.1.5 on 2025-01-18 17:39

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_human_change_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='human',
            name='education_level',
        ),
        migrations.AddField(
            model_name='human',
            name='birth_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

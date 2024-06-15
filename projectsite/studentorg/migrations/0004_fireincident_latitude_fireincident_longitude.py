# Generated by Django 5.0.4 on 2024-06-01 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentorg', '0003_firestation'),
    ]

    operations = [
        migrations.AddField(
            model_name='fireincident',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='fireincident',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
    ]

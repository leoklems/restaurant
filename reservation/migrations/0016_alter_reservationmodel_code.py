# Generated by Django 4.1.1 on 2023-01-14 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0015_reservationmodel_mode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservationmodel',
            name='code',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]

# Generated by Django 4.1.1 on 2023-01-14 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0003_rename_status_reservationmodel_confirmation_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservationmodel',
            name='confirmation_status',
            field=models.CharField(choices=[('confirmed', 'CONFIRMED'), ('pending', 'PENDING')], default='confirmed', max_length=20),
        ),
    ]

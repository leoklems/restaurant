# Generated by Django 4.1.1 on 2023-01-13 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservationmodel',
            name='email',
            field=models.EmailField(default='odeke@gmail.com', max_length=254),
            preserve_default=False,
        ),
    ]
# Generated by Django 4.1.1 on 2023-01-17 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallerymodel',
            name='title',
            field=models.CharField(default='sss', max_length=250),
            preserve_default=False,
        ),
    ]

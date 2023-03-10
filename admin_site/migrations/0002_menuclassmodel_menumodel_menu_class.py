# Generated by Django 4.1.5 on 2023-01-12 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_site', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuClassModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='menumodel',
            name='menu_class',
            field=models.ManyToManyField(blank=True, to='admin_site.menuclassmodel'),
        ),
    ]

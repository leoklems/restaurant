# Generated by Django 4.1.5 on 2023-01-12 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_site', '0002_menuclassmodel_menumodel_menu_class'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menumodel',
            name='category',
        ),
        migrations.RemoveField(
            model_name='menumodel',
            name='menu_class',
        ),
        migrations.DeleteModel(
            name='MenuCategoryModel',
        ),
        migrations.DeleteModel(
            name='MenuClassModel',
        ),
        migrations.DeleteModel(
            name='MenuModel',
        ),
    ]

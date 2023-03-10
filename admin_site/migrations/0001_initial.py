# Generated by Django 4.1.5 on 2023-01-12 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuCategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SiteInfoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('logo', models.FileField(blank=True, null=True, upload_to='images/logo')),
                ('mobile_1', models.CharField(blank=True, max_length=20, null=True)),
                ('mobile_2', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('whatsapp', models.CharField(blank=True, max_length=30, null=True)),
                ('working_hour', models.CharField(blank=True, max_length=100, null=True)),
                ('facebook_link', models.URLField(blank=True, null=True)),
                ('instagram_link', models.URLField(blank=True, null=True)),
                ('twitter_link', models.URLField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MenuModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_type', models.CharField(choices=[('food', 'FOOD'), ('drink', 'DRINK')], max_length=20)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('key', models.TextField(blank=True, null=True)),
                ('image', models.FileField(upload_to='images/menu')),
                ('status', models.CharField(choices=[('active', 'ACTIVE'), ('inactive', 'INACTIVE')], max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_site.menucategorymodel')),
            ],
        ),
    ]

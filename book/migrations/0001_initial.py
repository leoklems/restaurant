# Generated by Django 4.1.1 on 2023-01-17 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookCategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='BookModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(blank=True, max_length=250, null=True)),
                ('name', models.CharField(max_length=200)),
                ('image', models.FileField(upload_to='images/book')),
                ('description', models.TextField()),
                ('status', models.CharField(blank=True, choices=[('confirmed', 'CONFIRMED'), ('pending', 'PENDING')], default='confirmed', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.bookcategorymodel')),
            ],
        ),
    ]

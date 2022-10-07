# Generated by Django 4.1.2 on 2022-10-07 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('location', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='persons',
        ),
    ]

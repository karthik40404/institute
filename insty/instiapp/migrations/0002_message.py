# Generated by Django 5.1.2 on 2024-11-26 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instiapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
    ]

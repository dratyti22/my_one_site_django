# Generated by Django 4.2.10 on 2024-03-09 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Номер телефона'),
        ),
    ]

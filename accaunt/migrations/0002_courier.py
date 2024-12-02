# Generated by Django 5.1 on 2024-12-02 10:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accaunt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_type', models.CharField(blank=True, choices=[('bike', 'Bike'), ('car', 'Car'), ('scooter', 'Scooter')], help_text='Transport vositasini kiriting: ', max_length=50, null=True)),
                ('license_plate', models.CharField(blank=True, help_text='Avtomobil raqamini kiriting: ', max_length=20, null=True)),
                ('availability', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='courier_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Courier',
                'verbose_name_plural': 'Couriers',
            },
        ),
    ]

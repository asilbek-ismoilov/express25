# Generated by Django 5.1.2 on 2024-11-11 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accaunt', '0003_remove_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(db_index=True, default=1, max_length=254, unique=True),
            preserve_default=False,
        ),
    ]
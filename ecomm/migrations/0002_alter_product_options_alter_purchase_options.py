# Generated by Django 5.0.4 on 2024-04-17 00:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecomm', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterModelOptions(
            name='purchase',
            options={'ordering': ['-created_at']},
        ),
    ]

# Generated by Django 5.0.7 on 2024-08-23 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='number_ordered',
            new_name='quantity',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='number_of_products',
            new_name='quantity',
        ),
    ]

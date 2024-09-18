# Generated by Django 5.0.7 on 2024-08-25 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='customer',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='full_name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]

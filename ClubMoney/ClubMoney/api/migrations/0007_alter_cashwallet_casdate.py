# Generated by Django 4.1.3 on 2023-02-24 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_cashwallet_bidding'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cashwallet',
            name='casdate',
            field=models.DateField(auto_now=True),
        ),
    ]

# Generated by Django 4.1.3 on 2023-02-28 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_withdrawmoney'),
    ]

    operations = [
        migrations.AddField(
            model_name='rounds',
            name='Payment_status',
            field=models.BooleanField(default=False),
        ),
    ]
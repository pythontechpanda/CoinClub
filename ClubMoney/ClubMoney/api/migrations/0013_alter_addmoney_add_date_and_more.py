# Generated by Django 4.1.3 on 2023-02-28 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_addmoney_add_date_withdrawmoney_withdraw_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addmoney',
            name='add_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='withdrawmoney',
            name='withdraw_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

# Generated by Django 4.1.3 on 2023-03-09 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_remove_cashwallet_is_withdraw_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AmountTrasferTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_tran', models.CharField(max_length=200)),
                ('commission', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='AvgTrasferTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trasfertime', models.CharField(max_length=200)),
                ('commission', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ClubClosedTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clubclose', models.CharField(max_length=200)),
                ('commission', models.CharField(max_length=200)),
            ],
        ),
    ]

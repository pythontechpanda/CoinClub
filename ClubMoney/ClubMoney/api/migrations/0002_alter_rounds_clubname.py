# Generated by Django 4.1.3 on 2023-02-17 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rounds',
            name='clubname',
            field=models.CharField(max_length=50),
        ),
    ]

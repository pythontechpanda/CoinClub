# Generated by Django 4.1.3 on 2023-02-21 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_club_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='rounds',
            name='duration',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='rounds',
            name='startdate',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='rounds',
            name='starttime',
            field=models.TimeField(null=True),
        ),
    ]

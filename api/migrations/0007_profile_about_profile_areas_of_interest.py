# Generated by Django 4.2.7 on 2023-11-30 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_rename_profiles_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='about',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='areas_of_interest',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]

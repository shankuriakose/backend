# Generated by Django 4.2.7 on 2023-11-28 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_profiles_about_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profiles',
            name='start_date',
        ),
    ]
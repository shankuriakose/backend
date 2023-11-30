# Generated by Django 4.2.7 on 2023-11-28 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='comments',
            new_name='about',
        ),
        migrations.RemoveField(
            model_name='project',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='project',
            name='status',
        ),
        migrations.AddField(
            model_name='project',
            name='areas_of_interest',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='designation',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='organisation',
            field=models.CharField(max_length=100, null=True),
        ),
    ]

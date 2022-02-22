# Generated by Django 2.2.13 on 2022-02-15 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lost_and_found', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lostandfound',
            name='status',
        ),
        migrations.RemoveField(
            model_name='lostandfound',
            name='time',
        ),
        migrations.AddField(
            model_name='lostandfound',
            name='drive_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lostandfound',
            name='type_of_lost_and_found',
            field=models.CharField(choices=[('Lost', 'Lost'), ('Found', 'Found')], default=1, max_length=10),
            preserve_default=False,
        ),
    ]
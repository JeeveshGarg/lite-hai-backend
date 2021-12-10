# Generated by Django 2.2.13 on 2021-12-06 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=60)),
                ('year_of_joining', models.CharField(max_length=10)),
                ('schedule_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='ProffsAndHODs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=60)),
                ('year_of_joining', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='StudyMaterials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resource_url', models.URLField()),
            ],
        ),
    ]

# Generated by Django 4.0.5 on 2022-07-21 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manualupload', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='rollno',
            field=models.IntegerField(unique=True),
        ),
    ]
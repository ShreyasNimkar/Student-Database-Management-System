# Generated by Django 4.0.5 on 2022-07-21 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('rollno', models.IntegerField()),
                ('grade', models.IntegerField()),
                ('division', models.CharField(max_length=1)),
                ('mobno', models.CharField(max_length=12)),
            ],
        ),
    ]

# Generated by Django 2.0.13 on 2019-05-14 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=40)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('post', models.CharField(max_length=20)),
            ],
        ),
    ]

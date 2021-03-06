# Generated by Django 4.0.4 on 2022-05-24 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('genre', models.IntegerField()),
                ('rating', models.FloatField()),
                ('user_ratings_total', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('place_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('vicinity', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
    ]

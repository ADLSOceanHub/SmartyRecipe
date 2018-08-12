# Generated by Django 2.0.5 on 2018-08-12 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('ingredientid', models.AutoField(primary_key=True,
                                                  serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Measure',
            fields=[
                ('measureid', models.AutoField(primary_key=True,
                                               serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=255)),
                ('short_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('recipeid', models.AutoField(primary_key=True,
                                              serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
    ]
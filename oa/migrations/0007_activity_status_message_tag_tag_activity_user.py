# Generated by Django 2.2 on 2019-04-15 08:54

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oa', '0006_activity'),
    ]

    operations = [
        migrations.CreateModel(
            name='activity_status',
            fields=[
                ('activity_status_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('activity_status_name', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='message',
            fields=[
                ('message_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('author_id', models.BigIntegerField()),
                ('activity_id', models.BigIntegerField()),
                ('created', models.DateField()),
                ('message', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='tag',
            fields=[
                ('tag_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('tag_name', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='tag_activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activities_id', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
                ('tag_id', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.BigIntegerField()),
                ('login', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('nickname', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('isAdmin', models.BooleanField()),
            ],
        ),
    ]

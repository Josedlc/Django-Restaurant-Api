# Generated by Django 3.2.9 on 2021-11-20 00:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Direction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('pc', models.CharField(max_length=20)),
                ('street', models.CharField(max_length=60)),
                ('int_number', models.IntegerField()),
                ('ext_number', models.IntegerField()),
                ('state', models.TimeField()),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant_types',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=130)),
                ('schedule_open', models.TimeField()),
                ('schedule_close', models.TimeField()),
                ('phone_number', models.CharField(max_length=12)),
                ('direction', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='restaurants.direction')),
                ('restaurant_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='restaurants.restaurant_types')),
            ],
        ),
    ]

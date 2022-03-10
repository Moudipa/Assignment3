# Generated by Django 3.2.12 on 2022-02-20 19:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('brand', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=1, max_digits=10)),
                ('in_stock', models.IntegerField()),
                ('ratings', models.DecimalField(decimal_places=1, max_digits=2)),
                ('supplier', models.CharField(max_length=200)),
                ('needs_prescription', models.BooleanField(default=False)),
                ('image', models.ImageField(upload_to='photos/')),
                ('listed_on', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]

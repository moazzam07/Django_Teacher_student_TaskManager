# Generated by Django 4.0.5 on 2022-06-26 20:10

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
                ('email', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('country', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('country', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('experience', models.IntegerField()),
            ],
        ),
    ]

# Generated by Django 2.2 on 2019-04-26 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='douban',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('intro', models.CharField(max_length=255)),
                ('date', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=255)),
                ('Press', models.CharField(max_length=255)),
                ('point', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='jingdong',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ititle', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=255)),
                ('intro', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='tianqiyubao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=255)),
                ('date', models.CharField(max_length=255)),
                ('weather', models.CharField(max_length=255)),
                ('temp', models.CharField(max_length=255)),
            ],
        ),
    ]
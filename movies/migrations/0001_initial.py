# Generated by Django 3.1.7 on 2021-03-30 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('address', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('desc', models.TextField(max_length=500)),
                ('year', models.DateField()),
                ('rate', models.IntegerField()),
                ('poster', models.ImageField(upload_to='movies/posters')),
                ('video', models.FileField(upload_to='movies/video')),
                ('cast', models.ManyToManyField(to='movies.Cast')),
                ('categories', models.ManyToManyField(to='movies.Category')),
            ],
        ),
    ]

# Generated by Django 3.1.7 on 2021-03-30 22:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_movie_cast'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='movies.country'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='rate',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='movies.rate'),
        ),
    ]

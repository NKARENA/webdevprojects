# Generated by Django 3.2.9 on 2021-12-25 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('releasedate', models.DateField()),
                ('moviename', models.CharField(max_length=30)),
                ('hero', models.CharField(max_length=30)),
                ('IMDB', models.IntegerField()),
            ],
        ),
    ]

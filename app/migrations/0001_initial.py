# Generated by Django 2.0.2 on 2018-09-16 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('food_stuff', models.TextField(blank=True)),
                ('name', models.TextField(blank=True)),
                ('link', models.TextField(blank=True)),
                ('text', models.TextField(blank=True)),
            ],
        ),
    ]

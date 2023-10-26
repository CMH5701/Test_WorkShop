# Generated by Django 4.2.6 on 2023-10-19 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WorkShop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=30)),
                ('pub_date', models.DateTimeField()),
                ('likes', models.PositiveIntegerField(default=0)),
                ('dislikes', models.IntegerField(default=0)),
                ('sadness', models.IntegerField(default=0)),
            ],
        ),
    ]
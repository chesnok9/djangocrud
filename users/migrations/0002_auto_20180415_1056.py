# Generated by Django 2.0.4 on 2018-04-15 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='random_number',
            field=models.IntegerField(default=69),
        ),
    ]

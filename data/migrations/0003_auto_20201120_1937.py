# Generated by Django 3.1.1 on 2020-11-20 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_auto_20201019_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='detail',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]

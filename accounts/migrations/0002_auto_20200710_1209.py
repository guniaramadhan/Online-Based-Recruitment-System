# Generated by Django 2.2.6 on 2020-07-10 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='vacancy',
            field=models.CharField(max_length=50),
        ),
    ]

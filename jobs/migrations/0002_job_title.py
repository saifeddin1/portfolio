# Generated by Django 2.2.2 on 2020-01-14 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='title',
            field=models.CharField(default='', max_length=50),
        ),
    ]

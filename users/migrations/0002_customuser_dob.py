# Generated by Django 3.0.1 on 2020-11-08 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='DOB',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]

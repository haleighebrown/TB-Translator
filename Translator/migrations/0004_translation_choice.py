# Generated by Django 3.0.1 on 2020-11-07 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Translator', '0003_auto_20201107_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='translation',
            name='choice',
            field=models.CharField(default='Text to Binary', max_length=154),
        ),
    ]
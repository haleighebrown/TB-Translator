# Generated by Django 3.0.1 on 2020-11-07 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Translator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='translation',
            name='body',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='translation',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='translation',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]

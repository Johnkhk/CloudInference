# Generated by Django 4.0.3 on 2022-04-08 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('benlp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='summarizer',
            name='context',
            field=models.TextField(),
        ),
    ]

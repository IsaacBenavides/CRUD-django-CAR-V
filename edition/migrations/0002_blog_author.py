# Generated by Django 4.0.3 on 2022-03-29 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edition', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
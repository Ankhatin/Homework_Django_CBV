# Generated by Django 5.0.7 on 2024-07-28 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='count_review',
            field=models.IntegerField(default=0),
        ),
    ]
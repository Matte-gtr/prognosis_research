# Generated by Django 3.2 on 2021-04-22 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whats_new', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='research_update',
            name='link_name',
            field=models.CharField(blank=True, max_length=56),
        ),
    ]

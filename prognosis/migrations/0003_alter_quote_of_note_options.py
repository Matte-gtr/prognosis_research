# Generated by Django 3.2 on 2021-04-30 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prognosis', '0002_alter_quote_of_note_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quote_of_note',
            options={'verbose_name': 'Quote of note', 'verbose_name_plural': 'Quotes of note'},
        ),
    ]

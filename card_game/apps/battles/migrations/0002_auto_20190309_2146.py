# Generated by Django 2.1.7 on 2019-03-09 21:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('battles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='battleround',
            old_name='round_results',
            new_name='results',
        ),
    ]

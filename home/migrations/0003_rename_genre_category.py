# Generated by Django 3.2 on 2021-04-14 03:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210413_2226'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Genre',
            new_name='Category',
        ),
    ]

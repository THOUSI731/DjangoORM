# Generated by Django 4.2.2 on 2023-07-01 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ormapp', '0003_category2_hero'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category2',
            new_name='CategoryHero',
        ),
    ]

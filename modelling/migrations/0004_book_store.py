# Generated by Django 4.2.2 on 2023-07-25 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelling', '0003_department_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=308)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=308)),
                ('books', models.ManyToManyField(to='modelling.book')),
            ],
        ),
    ]

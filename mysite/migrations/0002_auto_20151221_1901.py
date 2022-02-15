# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('classroom', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=60)),
                ('time', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=40)),
                ('office', models.CharField(max_length=40)),
                ('phone', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.RenameModel(
            old_name='Author',
            new_name='Student',
        ),
        migrations.RemoveField(
            model_name='book',
            name='authors',
        ),
        migrations.RemoveField(
            model_name='book',
            name='publisher',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='Publisher',
        ),
        migrations.AddField(
            model_name='course',
            name='student',
            field=models.ManyToManyField(to='mysite.Student'),
        ),
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(to='mysite.Teacher', on_delete=models.CASCADE),
        ),
    ]

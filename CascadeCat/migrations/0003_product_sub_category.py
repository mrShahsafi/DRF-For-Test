# Generated by Django 3.1.4 on 2021-01-20 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CascadeCat', '0002_auto_20210120_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sub_category',
            field=models.ManyToManyField(to='CascadeCat.SubCategory', verbose_name='Sub-Category'),
        ),
    ]

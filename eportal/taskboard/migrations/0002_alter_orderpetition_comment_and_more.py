# Generated by Django 4.2.7 on 2023-11-24 05:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderpetition',
            name='comment',
            field=models.TextField(help_text='Enter a  description of the yours order', max_length=1000),
        ),
        migrations.AlterField(
            model_name='orderpetition',
            name='design_image',
            field=models.ImageField(upload_to='design/%Y/%m/%d/', validators=[django.core.validators.validate_image_file_extension, django.core.validators.FileExtensionValidator(['bmp', 'jpg', 'jpeg', 'png'], message='Allowed datatypes:bmp,jpg,jpeg,png')]),
        ),
    ]

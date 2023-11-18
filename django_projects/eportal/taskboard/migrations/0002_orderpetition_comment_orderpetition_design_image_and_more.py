# Generated by Django 4.2.7 on 2023-11-18 03:31

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taskboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderpetition',
            name='comment',
            field=models.TextField(blank=True, help_text='Enter a  description of the yours order', max_length=1000),
        ),
        migrations.AddField(
            model_name='orderpetition',
            name='design_image',
            field=models.ImageField(blank=True, upload_to='design/%Y/%m/%d/', validators=[django.core.validators.validate_image_file_extension, django.core.validators.FileExtensionValidator(['bmp', 'jpg', 'jpeg', 'png'], message='Allowed datatypes:bmp,jpg,jpeg,png')]),
        ),
        migrations.AlterField(
            model_name='orderpetition',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='taskboard.category'),
        ),
    ]

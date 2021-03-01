# Generated by Django 3.1.5 on 2021-03-01 22:22

import django.core.validators
from django.db import migrations, models
import music_publisher.validators


class Migration(migrations.Migration):

    dependencies = [
        ('music_publisher', '0004_auto_20210209_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='writer',
            name='publisher_fee',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='writer',
            name='saan',
            field=models.CharField(blank=True, help_text='Use this field for a general original publishing agreement.', max_length=14, null=True, unique=True, validators=[music_publisher.validators.CWRFieldValidator('saan')], verbose_name='SAAN'),
        ),
        migrations.AlterField(
            model_name='writerinwork',
            name='saan',
            field=models.CharField(blank=True, help_text='Use this field for specific agreements only.For general agreements use the field in the Writer form.', max_length=14, null=True, validators=[music_publisher.validators.CWRFieldValidator('saan')], verbose_name='Society-assigned specific agreement number'),
        ),
    ]

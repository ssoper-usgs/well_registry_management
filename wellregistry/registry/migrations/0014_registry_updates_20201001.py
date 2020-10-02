# The below suppresses pylint message: Module name "*" doesn't conform to snake_case naming style
# pylint: disable-msg=C0103
# Enable check for the rest of the file
# pylint: enable-msg=C0103
"""
 Updating fields including well depth which did not allow for well depths over 100)
"""
# Generated by Django 3.1 on 2020-10-01 18:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    """
    Minor changes to fields
    """

    dependencies = [
        ('registry', '0013_registry_update_well_depth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monitoringlocation',
            name='site_name',
            field=models.CharField(max_length=300, validators=[django.core.validators.RegexValidator('\\S[\\s\\S]*', message='Field must not be blank')]),
        ),
        migrations.AlterField(
            model_name='monitoringlocation',
            name='site_no',
            field=models.CharField(max_length=16, validators=[django.core.validators.RegexValidator('\\S[\\s\\S]*', message='Field must not be blank')]),
        ),
        migrations.AlterField(
            model_name='monitoringlocation',
            name='well_depth',
            field=models.DecimalField(blank=True, decimal_places=7, max_digits=11, null=True),
        ),
    ]

# The below suppresses pylint message: Module name "0005_lookups_fk" doesn't conform to snake_case naming style
# pylint: disable-msg=C0103
# Enable check for the rest of the file
# pylint: enable-msg=C0103
"""
# Data migration to cleanup foreign keys in state and country tables. Add unit_id column to units table.
"""
# Generated by Django 3.0.7 on 2020-07-10 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):


    dependencies = [
        ('registry', '0004_lookup_tables'),
    ]

    operations = [
        migrations.AddField(
            model_name='countylookup',
            name='state_id',
            field=models.ForeignKey(db_column='state_id', on_delete=django.db.models.deletion.PROTECT,
                                    to='registry.StateLookup'),
        ),
        migrations.AddField(
            model_name='unitslookup',
            name='unit_id',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='countylookup',
            name='country_cd',
            field=models.ForeignKey(db_column='country_cd', on_delete=django.db.models.deletion.PROTECT,
                                    to='registry.CountryLookup', to_field='country_cd'),
        ),
        migrations.AlterField(
            model_name='statelookup',
            name='country_cd',
            field=models.ForeignKey(db_column='country_cd', on_delete=django.db.models.deletion.PROTECT,
                                    to='registry.CountryLookup', to_field='country_cd'),
        ),
        migrations.AlterUniqueTogether(
            name='countylookup',
            unique_together={('country_cd', 'state_id', 'county_cd')},
        ),
        migrations.RemoveField(
            model_name='countylookup',
            name='state_cd',
        ),
    ]
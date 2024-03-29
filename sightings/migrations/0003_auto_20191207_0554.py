# Generated by Django 2.2.7 on 2019-12-07 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0002_auto_20191207_0347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squirrel_site',
            name='Approaches',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='squirrel_site',
            name='Chasing',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='squirrel_site',
            name='Climbing',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='squirrel_site',
            name='Date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='squirrel_site',
            name='Eating',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='squirrel_site',
            name='Foraging',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='squirrel_site',
            name='Indifferent',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='squirrel_site',
            name='Kuks',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='squirrel_site',
            name='Moans',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='squirrel_site',
            name='Other_activities',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='squirrel_site',
            name='Other_interactions',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='squirrel_site',
            name='Quaas',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='squirrel_site',
            name='Running',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='squirrel_site',
            name='Runs_from',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='squirrel_site',
            name='Specific_location',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='squirrel_site',
            name='Tail_flags',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='squirrel_site',
            name='Tail_twitches',
            field=models.BooleanField(default=False),
        ),
    ]

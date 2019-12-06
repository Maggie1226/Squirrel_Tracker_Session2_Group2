
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='squirrel_site',
            fields=[
                ('Latitude', models.FloatField(max_length=100)),
                ('Longtitude', models.FloatField(max_length=100)),
                ('Unique_Squirrel_ID', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('Shift', models.CharField(choices=[('AM', 'AM'), ('PM', 'PM')], default='AM', max_length=2)),
                ('Date', models.CharField(max_length=10)),
                ('Age', models.CharField(choices=[('Adult', 'Adult'), ('Juvenile', 'Juvenile')], default='Adult', max_length=10)),
                ('Primary_fur_color', models.CharField(choices=[('Gray', 'Gray'), ('Cinnamon', 'Cinnamon'), ('Black', 'Black')], default='Gray', max_length=10)),
                ('Location', models.CharField(choices=[('GP', 'Ground Plane'), ('AG', 'Above Ground')], default='GP', max_length=20)),
                ('Specific_location', models.TextField(max_length=500)),
                ('Running', models.BooleanField(default=True)),
                ('Chasing', models.BooleanField(default=True)),
                ('Climbing', models.BooleanField(default=True)),
                ('Eating', models.BooleanField(default=True)),
                ('Foraging', models.BooleanField(default=True)),
                ('Other_activities', models.TextField(max_length=500)),
                ('Kuks', models.BooleanField(default=True)),
                ('Quaas', models.BooleanField(default=True)),
                ('Moans', models.BooleanField(default=True)),
                ('Tail_flags', models.BooleanField(default=True)),
                ('Tail_twitches', models.BooleanField(default=True)),
                ('Approaches', models.BooleanField(default=True)),
                ('Indifferent', models.BooleanField(default=True)),
                ('Runs_from', models.BooleanField(default=True)),
                ('Other_interactions', models.TextField(max_length=500)),
            ],
        ),
    ]
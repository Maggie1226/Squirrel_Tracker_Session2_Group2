# Generated by Django 2.2.7 on 2019-12-07 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0003_auto_20191207_0554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squirrel_site',
            name='Age',
            field=models.CharField(choices=[('adult', 'Adult'), ('juvenile', 'Juvenile')], default='adult', help_text='Value is either "Adult" or "Juvenile."', max_length=10),
        ),
        migrations.AlterField(
            model_name='squirrel_site',
            name='Approaches',
            field=models.BooleanField(default=False, help_text='Squirrel was seen approaching human, seeking food.'),
        ),
        migrations.AlterField(
            model_name='squirrel_site',
            name='Date',
            field=models.DateField(help_text='Concatenation of the sighting session day and month.'),
        ),
        migrations.AlterField(
            model_name='squirrel_site',
            name='Indifferent',
            field=models.BooleanField(default=False, help_text='Squirrel was indifferent to human presence.'),
        ),
        migrations.AlterField(
            model_name='squirrel_site',
            name='Kuks',
            field=models.BooleanField(default=False, help_text='xSquirrel was heard kukking, a chirpy vocal communication used for a variety of reasons.'),
        ),
        migrations.AlterField(
            model_name='squirrel_site',
            name='Location',
            field=models.CharField(choices=[('GP', 'Ground Plane'), ('AG', 'Above Ground')], default='GP', help_text='the location of where the squirrel was when first sighted.', max_length=20),
        ),
        migrations.AlterField(
            model_name='squirrel_site',
            name='Moans',
            field=models.BooleanField(default=False, help_text='Squirrel was heard moaning, a high-pitched vocal communication which can indicate the presence of an air predator such as a hawk.'),
        ),
        migrations.AlterField(
            model_name='squirrel_site',
            name='Other_interactions',
            field=models.TextField(blank=True, help_text='Sighter notes on other types of interactions between squirrels and humans.', max_length=500),
        ),
        migrations.AlterField(
            model_name='squirrel_site',
            name='Primary_fur_color',
            field=models.CharField(choices=[('gray', 'Gray'), ('cinnamon', 'Cinnamon'), ('black', 'Black')], default='gray', max_length=10),
        ),
        migrations.AlterField(
            model_name='squirrel_site',
            name='Quaas',
            field=models.BooleanField(default=False, help_text='Squirrel was heard quaaing, an elongated vocal communication which can indicate the presence of a ground predator such as a dog.'),
        ),
        migrations.AlterField(
            model_name='squirrel_site',
            name='Runs_from',
            field=models.BooleanField(default=False, help_text='Squirrel was seen running from humans, seeing them as a threat'),
        ),
        migrations.AlterField(
            model_name='squirrel_site',
            name='Shift',
            field=models.CharField(choices=[('am', 'AM'), ('pm', 'PM')], default='am', help_text='Value is either "AM" or "PM," to communicate whether or not the sighting session occurred in the morning or late afternoon.', max_length=2),
        ),
        migrations.AlterField(
            model_name='squirrel_site',
            name='Specific_location',
            field=models.TextField(blank=True, help_text='Sighters occasionally added commentary on the squirrel location. These notes are provided here.', max_length=500),
        ),
        migrations.AlterField(
            model_name='squirrel_site',
            name='Tail_flags',
            field=models.BooleanField(default=False, help_text="Squirrel was seen flagging its tail. Flagging is a whipping motion used to exaggerate squirrel's size and confuse rivals or predators. Looks as if the squirrel is scribbling with tail into the air."),
        ),
        migrations.AlterField(
            model_name='squirrel_site',
            name='Tail_twitches',
            field=models.BooleanField(default=False, help_text='Squirrel was seen twitching its tail. Looks like a wave running through the tail, like a breakdancer doing the arm wave. Often used to communicate interest, curiosity.'),
        ),
        migrations.AlterField(
            model_name='squirrel_site',
            name='Unique_Squirrel_ID',
            field=models.CharField(help_text='Identification tag for each squirrel sightings. The tag is comprised of "Hectare ID" + "Shift" + "Date" + "Hectare Squirrel Number."', max_length=20, primary_key=True, serialize=False, unique=True),
        ),
    ]
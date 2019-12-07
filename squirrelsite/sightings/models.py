from django.db import models

class squirrel_site(models.Model):
    Latitude=models.FloatField(max_length=100,)
    
    Longitude=models.FloatField(max_length=100,)
    
    Unique_Squirrel_ID=models.CharField(
        max_length=20,
        primary_key=True,
        unique=True,
        help_text='Identification tag for each squirrel sightings. The tag is comprised of "Hectare ID" + "Shift" + "Date" + "Hectare Squirrel Number."',
        )
    
    AM="am"
    PM="pm"
    Shift_CHOICES=[(AM,"AM"),(PM,"PM"),]
    Shift=models.CharField(
        max_length=2,
        choices=Shift_CHOICES,
        default=AM,
        help_text='Value is either "AM" or "PM," to communicate whether or not the sighting session occurred in the morning or late afternoon.',
        )
    
    Date=models.DateField(
        auto_now=False,
        help_text='Concatenation of the sighting session day and month.',
        )
    
    ADULT="adult"
    JUVENILE="juvenile"
    Age_CHOICES=[(ADULT,"Adult"),(JUVENILE,"Juvenile"),]
    Age=models.CharField(
        max_length=10,
        choices=Age_CHOICES,
        default=ADULT,
        help_text='Value is either "Adult" or "Juvenile."',
        )
    
    GRAY="gray"
    CINNAMON="cinnamon"
    BLACK="black"
    Fur_CHOICES=[(GRAY,"Gray"),(CINNAMON,"Cinnamon"),(BLACK,"Black"),]
    Primary_fur_color=models.CharField(
        max_length=10,
        choices=Fur_CHOICES,
        default=GRAY,
        )
    
    Ground_Plane="GP"
    Above_Ground="AG"
    Location_CHOICES=[(Ground_Plane,"Ground Plane"),(Above_Ground,"Above Ground"),]
    Location=models.CharField(
        max_length=20,
        choices=Location_CHOICES,
        default=Ground_Plane,
        help_text ='the location of where the squirrel was when first sighted.',
        )

    Specific_location=models.TextField(
        max_length=500,
        blank=True,
        help_text='Sighters occasionally added commentary on the squirrel location. These notes are provided here.',
        )
    
    Running=models.BooleanField(
        default=False,
        )

    Chasing=models.BooleanField(
        default=False,
        )

    Climbing=models.BooleanField(
        default=False,
        )

    Eating=models.BooleanField(
        default=False,
        )

    Foraging=models.BooleanField(
        default=False,
        )

    Other_activities=models.TextField(
        max_length=500,
        blank=True,
        )

    Kuks=models.BooleanField(
        default=False,
        help_text='xSquirrel was heard kukking, a chirpy vocal communication used for a variety of reasons.'
        ,)

    Quaas=models.BooleanField(
        default=False,
        help_text='Squirrel was heard quaaing, an elongated vocal communication which can indicate the presence of a ground predator such as a dog.',
        )

    Moans=models.BooleanField(
        default=False,
        help_text='Squirrel was heard moaning, a high-pitched vocal communication which can indicate the presence of an air predator such as a hawk.',
        )

    Tail_flags=models.BooleanField(
        default=False,
        help_text="Squirrel was seen flagging its tail. Flagging is a whipping motion used to exaggerate squirrel's size and confuse rivals or predators. Looks as if the squirrel is scribbling with tail into the air.",
        )

    Tail_twitches=models.BooleanField(
        default=False,
        help_text='Squirrel was seen twitching its tail. Looks like a wave running through the tail, like a breakdancer doing the arm wave. Often used to communicate interest, curiosity.',
        )

    Approaches=models.BooleanField(
        default=False,
        help_text='Squirrel was seen approaching human, seeking food.',
        )

    Indifferent=models.BooleanField(
        default=False,
        help_text='Squirrel was indifferent to human presence.',
        )

    Runs_from=models.BooleanField(
        default=False,
        help_text='Squirrel was seen running from humans, seeing them as a threat',
        )

    Other_interactions=models.TextField(
        max_length=500,
        blank=True,
        help_text='Sighter notes on other types of interactions between squirrels and humans.',
        )



from django.core.management.base import BaseCommand
from sightings.models import squirrel_site
import csv
import datetime 
class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_file')
        
    def handle(self, *args, **options):
        with open(options["csv_file"]) as fp:
            reader=csv.DictReader(fp)
            datas=list(reader)
        for data in datas:
            sq=squirrel_site(
                Latitude=data['y']
               ,Longitude=data['x']
               ,Unique_Squirrel_ID=data['unique_squirrel_id']
               ,Shift=data['shift']
               ,Date=datetime.datetime.strptime(data['date'],'%m%d%Y').date()
               
               ,Age=data['age']
               ,Primary_fur_color=data['primary_fur_color']
               ,Location=data['location']
               ,Specific_location=data['specific_location']
               ,Running=data['running'][0].upper()+data['running'][1:]
               ,Chasing=data['chasing'][0].upper()+data['chasing'][1:]
               ,Climbing=data['climbing'][0].upper()+data['climbing'][1:]
               ,Eating=data['eating'][0].upper()+data['eating'][1:]
               ,Foraging=data['foraging'][0].upper()+data['foraging'][1:]
               ,Other_activities=data['other_activities']
               ,Kuks=data['kuks'][0].upper()+data['kuks'][1:]
               ,Quaas=data['quaas'][0].upper()+data['quaas'][1:]
               ,Moans=data['moans'][0].upper()+data['moans'][1:]
               ,Tail_flags=data['tail_flags'][0].upper()+data['tail_flags'][1:]
               ,Tail_twitches=data['tail_twitches'][0].upper()+data['tail_twitches'][1:]
               ,Approaches=data['approaches'][0].upper()+data['approaches'][1:]
               ,Indifferent=data['indifferent'][0].upper()+data['indifferent'][1:]
               ,Runs_from=data['runs_from'][0].upper()+data['runs_from'][1:]
               ,Other_interactions=data['other_interactions'],              )
            sq.save()


from django.apps import apps
from django.core.management.base import BaseCommad, CommandError
from .models import Squirrel
import csv
import os

class Command(BaseCommand):
    help="Insert squirrel data from CSV file."
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.model_name=squirrel_site

    def get_current_app_path(self):
        return apps.get_app_config('sightings').path
    
    def get_csv_file(self,filename):
        app_path=self.get_current_app_path()
        file_path=os.path.join(app_path,"management","commands",filename)
        return file_path

    def add_arguments(self, parser):
        parser.add_argument('filenames',
                            nargs='+',
                            type=str,
                            help="Inserts squirrel data from CSV file")
    def insert_to_df(self,data):
        try:
            self.model_name.objects.create(
               Latitude = data['Latitude']
               ,Longtitude = data['Longtitude']
               ,Unique_Squirrel_ID= data['Unique_Squirrel_ID']
               ,Shift= data['Shift']
               ,Date = data['Date ']
               ,Age= data['Age']
               ,Primary_fur_color= data['Primary_fur_color']
               ,Location= data['Location']
               ,Specific_location= data['Specific_location']
               ,Running= data['Running' ]
               ,Chasing = data['Chasing'  ]
               ,Climbing = data['Climbing' ]
               ,Eating = data['Eating'   ]
               ,Foraging= data['Foraging' ]
               ,Other_activities= data['Other_activities']
               ,Kuks= data['Kuks']
               ,Quaas= data['Quaas']
               ,Moans= data['Moans']
               ,Tail_flags= data['Tail_flags']
               ,Tail_twitches= data['Tail_twitches']
               ,Approaches= data['Approaches']
               ,Indifferent= data['Indifferent']
               ,Runs_from= data['Runs_from']
               ,Other_interactions= data['Other_interactions']
            )
        except Exception as e:
            raise CommandError("Error in inserting {}: {}".format(
                self.model_name, str(e)))

    def handle(self, *args, **options):

        for filename in options['filenames']:
            self.stdout.write(self.style.SUCCESS('Reading:{}'.format(filename)))
            file_path = self.get_csv_file(filename)
            try:
                with open(file_path) as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter=',')
                    for row in csv_reader:
                        if row != "":
                            words = [word.strip() for word in row]
                            data = {}
                            data['Latitude' ]=word[0]                
                            data['Longtitude']=word[1]               
                            data['Unique_Squirrel_ID']=word[2]       
                            data['Shift']=word[4]              
                            data['Date ']=word[5]              
                            data['Age']=word[7]                
                            data['Primary_fur_color']=word[8]  
                            data['Location']=word[12]           
                            data['Specific_location']=word[14]  
                            data['Running' ]=word[15]           
                            data['Chasing'  ]=word[16]          
                            data['Climbing' ]=word[17]          
                            data['Eating'   ]=word[18]          
                            data['Foraging' ]=word[19]          
                            data['Other_activities']=word[20]   
                            data['Kuks']=word[21]               
                            data['Quaas']=word[22]              
                            data['Moans']=word[23]              
                            data['Tail_flags']=word[24]         
                            data['Tail_twitches']=word[25]            
                            data['Approaches']=word[26]               
                            data['Indifferent']=word[27]              
                            data['Runs_from']=word[28]                
                            data['Other_interactions']=word[29]       
                            self.insert_=_to_db(data)
                            self.stdout.write(
                                self.style.SUCCESS('{}'.format(
                                        word[2]
                                        )
                                )
                            )


            except FileNotFoundError:
                raise CommandError("File {} does not exist".format(
                    file_path))~                       

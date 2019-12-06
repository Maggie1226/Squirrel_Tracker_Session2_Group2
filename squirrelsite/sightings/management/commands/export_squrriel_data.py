from django.core.management.base import BaseCommand, CommandError
from django.apps import apps
from .models import Squirrel
import csv
import sys

class Command(BaseCommand):
    help = ("Output the  model as CSV")
    args = '[appname.ModelName]'

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
                            help="export squirrel data from model to CSV file")
   


    def handle(self, *app_labels, **options):
     	filename = options['filenames']
        field_names = [f.name for f in Squirrel._meta.fields]
        file= get_csv_file(filename)
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerow(field_names)
        for instance in Squirrel.objects.all():
            writer.writerow([unicode(getattr(instance, f)).encode('utf-8') for f in field_names])

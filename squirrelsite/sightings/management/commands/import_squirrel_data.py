from django.apps import apps
from django.core.management.base import BaseCommad, CommandError
from .models import Squirrel
import csv
import os

class Command(BaseCommand):
    help="Insert squirrel data from CSV file."
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.model_name=squirrel

    def get_current_app_path(self):
        return apps.get_app_config('sightings').path
    def get_csv_file(self,filename):
        app_path=self.get_current_app_path()
        file_path=os.path.join(app_path,"management","commands",filename)
        return file_path

    def add_arguments(self,parser):
        parser.add_argument('filenames',
                nargs="+",
                type=str,
                help="Inserts Squirrel data from CSV file."
        )

    def handle(self,*args,**options):
        if options['']

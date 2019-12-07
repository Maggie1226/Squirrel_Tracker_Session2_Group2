from django.core.management.base import BaseCommand
from sightings .models import squirrel_site
import csv

class Command(BaseCommand):
    def add_arguments(self,parser):
        parser.add_argument("csv_file")

    def handle(self, *args, **options):
        with open(options['csv_file'],"w",newline="") as fp:
            writer=csv.writer(fp,delimiter=",")
            field_names=[f.name for f in squirrel_site._meta.fields]
            writer.writerow(field_names)
            for obj in squirrel_site.objects.all():
                row=[]
                for field in field_names:
                    row.append(str(getattr(obj,field)))
                writer.writerow(row)

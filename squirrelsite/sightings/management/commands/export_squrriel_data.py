from django.core.management.base import BaseCommand
from .models import squirrel_site
import csv

class Command(BaseCommand):
    def add_arguments(self,parser):
        parser.add_arguments("csv_file")

    def get_model_fields(model):
        return model._meta.fields

    def handle(self, *args, **options):
        with open(options['csv_file'],"w",newline="") as fp:
            writer=csv.writer(fp)
            field_names=[f.name for f in get_model_fields(squirrel_site)]
            writer.writerow(field_names)
            for obj in squirrel_site.objects.all():
                row=""
                for field in field_names:
                    row+=unicode(getattr(obj,field)).encode("utf-8")+","
                writer.writerow(row)

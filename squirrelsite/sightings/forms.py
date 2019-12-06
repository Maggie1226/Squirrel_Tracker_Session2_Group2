from django.forms import ModelForm
from .models import squirrel_site

class SquirrelForm(ModelForm):
    class Meta:
        model=squirrel_site
        fields = '__all__'

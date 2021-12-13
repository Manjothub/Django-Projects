from django.forms import ModelForm
from . models import * 
class AddForm(ModelForm):
    class Meta:
        model=Addpost
        fields=['event_name' , 'data' , 'location','image']
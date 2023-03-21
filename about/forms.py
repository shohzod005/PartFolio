from django.forms import ModelForm
from .models import Cantact

class CantactForm(ModelForm):
    class Meta:
        model = Cantact
        fields = '__all__'
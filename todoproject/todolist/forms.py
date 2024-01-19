from .models import Task
from django.forms import ModelForm


class TaskForm(ModelForm):
        
    class Meta:
        model = Task
        fields = "__all__"
  
        labels = {
            'name': 'Название',
            'desc': 'Описание',
            'status_id': 'Статус'
        }

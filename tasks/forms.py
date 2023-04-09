from django import forms
from .models import Task
class TaskForm(forms.ModelForm):

    # Hint: this will need to be changed for use in the ads application :)
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'estimated_duration', 'priority', 'milestone']

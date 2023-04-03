from django import forms

class TaskForm(forms.ModelForm):
    pass
    # Hint: this will need to be changed for use in the ads application :)
    # class Meta:
    #     model = Ad
    #     fields = ['title', 'text', 'price', 'picture', 'tags']  # Picture is manual

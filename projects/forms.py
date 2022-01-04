from django.forms import ModelForm
from .models import Project
from django import forms
class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        widgets = {
            'tags':forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__()
        self.fields['title'].widget.attrs.update({'class':'input','placeholder':'Add Title'})
        self.fields['description'].widget.attrs.update({'class':'input','placeholder':'Add Title'})
        self.fields['demo_link'].widget.attrs.update({'class':'input','placeholder':'Add Title'})
        self.fields['source_link'].widget.attrs.update({'class':'input','placeholder':'Add Title'})
        self.fields['tags'].widget.attrs.update({'class':'input','placeholder':'Add Title'})
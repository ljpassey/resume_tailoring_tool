from django import forms
from .models import Resume

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['original_resume', 'job_description']
        widgets = {
            'job_description': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }


from django.db import models
from django.contrib.auth.models import User

class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resumes')
    original_resume = models.FileField(upload_to='resumes/')
    tailored_resume = models.FileField(upload_to='tailored_resumes/', blank=True, null=True)
    job_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s resume dated {self.created_at.strftime('%Y-%m-%d')}"

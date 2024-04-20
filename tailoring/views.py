from django.shortcuts import render, redirect
from .forms import ResumeForm
from .models import Resume
import openai

def extract_keywords(job_description):
    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=f"Extract keywords from this job description:\n\n{job_description}",
      max_tokens=60
    )
    return response.choices[0].text.strip()

def upload_resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.user = request.user  # Assuming user authentication
            keywords = extract_keywords(resume.job_description)
            resume.keywords = keywords  # Ensure your model has a field for keywords if you want to store them
            resume.save()
            return redirect('display_results', resume_id=resume.id)
    else:
        form = ResumeForm()
    return render(request, 'tailoring/upload_resume.html', {'form': form})

def display_results(request, resume_id):
    resume = Resume.objects.get(id=resume_id)
    return render(request, 'tailoring/display_results.html', {'resume': resume})


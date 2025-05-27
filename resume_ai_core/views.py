from django.shortcuts import render, redirect,get_object_or_404
from .forms import PersonalInfoForm, EducationForm, SkillForm, ProjectForm
from .models import PersonalInfo, Education, Skill, Project
from .openai_client import ask_openai
from .models import Resume

def resume_ai_chat(request, resume_id):
    resume = get_object_or_404(Resume, id=resume_id)
    answer = None
    if request.method == "POST":
        question = request.POST.get("question")
        # Combine resume data to prompt AI
        prompt = f"Resume:\nName: {resume.name}\nSummary: {resume.summary}\nSkills: {resume.skills}\nExperience: {resume.experience}\nEducation: {resume.education}\n\nQuestion: {question}\nAnswer:"
        answer = ask_openai(prompt)
    return render(request, "resume_ai_core/chat.html", {"resume": resume, "answer": answer})

def ai_resume_assistant(request):
    answer = None
    if request.method == 'POST':
        question = request.POST.get('question')

        # Example: gather some resume data (you can customize this)
        personal_info = PersonalInfo.objects.first()
        skills = Skill.objects.all()
        projects = Project.objects.all()

        # Prepare context data to send to AI
        context_text = f"Personal Info: {personal_info}\nSkills: {[skill.name for skill in skills]}\nProjects: {[project.title for project in projects]}"

        prompt = f"You are an assistant helping to answer questions about a resume.\nResume data:\n{context_text}\n\nQuestion: {question}\nAnswer:"

        answer = ask_openai(prompt)

    return render(request, 'resume_ai_core/ai_assistant.html', {'answer': answer})

def build_resume(request):
    if request.method == 'POST':
        p_form = PersonalInfoForm(request.POST)
        e_form = EducationForm(request.POST)
        s_form = SkillForm(request.POST)
        pr_form = ProjectForm(request.POST)

        if all([p_form.is_valid(), e_form.is_valid(), s_form.is_valid(), pr_form.is_valid()]):
            p_form.save()
            e_form.save()
            s_form.save()
            pr_form.save()
            return redirect('resume-list')
    else:
        p_form = PersonalInfoForm()
        e_form = EducationForm()
        s_form = SkillForm()
        pr_form = ProjectForm()

    context = {
        'p_form': p_form,
        'e_form': e_form,
        's_form': s_form,
        'pr_form': pr_form
    }
    return render(request, 'resume_ai_core/build_resume.html', context)

def resume_list(request):
    personal_infos = PersonalInfo.objects.all()
    educations = Education.objects.all()
    skills = Skill.objects.all()
    projects = Project.objects.all()

    context = {
        'personal_infos': personal_infos,
        'educations': educations,
        'skills': skills,
        'projects': projects,
    }
    return render(request, 'resume_ai_core/resume_list.html', context)


def home(request):
    return render(request, 'home.html')


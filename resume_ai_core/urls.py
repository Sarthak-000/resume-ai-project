from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
     path('build/', views.build_resume, name='build-resume'),
    path('list/', views.resume_list, name='resume-list'),
     path('ai-assistant/', views.ai_resume_assistant, name='ai_assistant'),
      path("resume/<int:resume_id>/chat/", views.resume_ai_chat, name="resume_ai_chat"),
]

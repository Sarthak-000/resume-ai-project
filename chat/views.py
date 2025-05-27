from django.shortcuts import render
from .forms import ChatForm
from resume_ai_core.openai_client import ask_openai  # reuse your OpenAI function

chat_history = []
def chat_view(request):
    global chat_history
    if request.method == "POST":
        prompt = request.POST.get("prompt")
        if prompt:
            response = ask_openai(prompt)
            chat_history.append({'sender': 'user', 'text': prompt})
            chat_history.append({'sender': 'ai', 'text': response})

    return render(request, "chat/index.html", {"chat_history": chat_history})

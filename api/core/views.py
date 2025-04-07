from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout
import requests
import os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from core.faqs import buscar_resposta_faq
from dotenv import load_dotenv
load_dotenv()


def register(request):
    if request.method == 'POST':
        # Verifica se a requisição tem um corpo JSON
        if request.content_type == 'application/json':
            try:
                data = json.loads(request.body)  # Converte JSON para dicionário Python
                form = CustomUserCreationForm(data)  # Passa os dados para o formulário
            except json.JSONDecodeError:
                return JsonResponse({"error": "JSON inválido"}, status=400)
        else:
            form = CustomUserCreationForm(request.POST)  # Se não for JSON, usa POST normal
        
        if form.is_valid():
            user = form.save()
            login(request, user)
            return JsonResponse({"message": "Cadastro realizado com sucesso!", "user": user.username}, status=201)
        else:
            return JsonResponse({"errors": form.errors}, status=400)

    # Se for uma requisição GET, exibe o formulário normalmente (para quem acessa via navegador)
    form = CustomUserCreationForm()
    return render(request, 'core/register.html', {'form': form})


def home(request):
    return render(request, 'core/index.html')

#@csrf_exempt#Para os testes no Postman retirar este comentário, para desativação do token CSRF
    if request.method == 'POST':
        # Verifica se a requisição tem um corpo JSON
        if request.content_type == 'application/json':
            try:
                data = json.loads(request.body)  # Converte JSON para dicionário Python
                form = CustomUserCreationForm(data)  # Passa os dados para o formulário
            except json.JSONDecodeError:
                return JsonResponse({"error": "JSON inválido"}, status=400)
        else:
            form = CustomUserCreationForm(request.POST)  # Se não for JSON, usa POST normal
        
        if form.is_valid():
            user = form.save()
            login(request, user)
            return JsonResponse({"message": "Cadastro realizado com sucesso!", "user": user.username}, status=201)
        else:
            return JsonResponse({"errors": form.errors}, status=400)

    # Se for uma requisição GET, exibe o formulário normalmente (para quem acessa via navegador)
    form = CustomUserCreationForm()
    return render(request, 'core/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redireciona para a página home após o login
        else:
            messages.error(request, 'Usuário ou senha incorretos.')
    return render(request, 'core/login.html')

def user_logout(request):
    logout(request)
    return redirect('home')



"""Testanto chatbot integrado com IA"""




def chatbot_page(request):
     return render(request, "core/chatbot.html")
 
 # Configuração do chatbot
API_URL = "https://openrouter.ai/api/v1/chat/completions"  # URL da API gratuita do OpenRouter
API_KEY = os.getenv("OPENROUTER_API_KEY")  # Pegamos a chave da API nas variáveis de ambiente
 
@csrf_exempt
def chatbot(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_message = data.get("message", "").strip()

            if not user_message:
                return JsonResponse({"error": "Mensagem vazia"}, status=400)

            # 🔍 1. Verifica se a pergunta está nas FAQs
            resposta_faq = buscar_resposta_faq(user_message)
            if resposta_faq:
                return JsonResponse({"response": resposta_faq})

            # 2. Chamada à API se não encontrou na FAQ
            response = requests.post(
                API_URL,
                headers={
                    "Authorization": f"Bearer {API_KEY}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": "openai/gpt-3.5-turbo",
                    "messages": [{"role": "user", "content": user_message}]
                }
            )

            ai_response = response.json()
            bot_reply = ai_response["choices"][0]["message"]["content"]

            return JsonResponse({"response": bot_reply})

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Método não permitido"}, status=405)
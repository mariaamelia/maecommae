from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout
import requests
import os


from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from core.faqs import buscar_resposta_faq
from dotenv import load_dotenv
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import ensure_csrf_cookie

load_dotenv()



@ensure_csrf_cookie
def csrf_cookie(request):
    return JsonResponse({'detail': 'CSRF cookie set'})

@csrf_exempt
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

from django.contrib.auth import get_user_model

User = get_user_model()

@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        try:
            if request.content_type == 'application/json':
                data = json.loads(request.body)
                email = data.get('email')
                password = data.get('password')

                try:
                    # Busca o usuário pelo e-mail e pega o username
                    user_obj = User.objects.get(email=email)
                    username = user_obj.username
                except User.DoesNotExist:
                    return JsonResponse({'errors': {'email': 'Usuário não encontrado.'}}, status=401)

                user = authenticate(request, username=username, password=password)

                if user is not None:
                    login(request, user)
                    return JsonResponse({'message': 'Login realizado com sucesso!','user': user.username }, status=200)
                else:
                    return JsonResponse({'errors': {'password': 'Senha incorreta.'}}, status=401)
            else:
                return JsonResponse({'error': 'Requisição deve ser JSON.'}, status=400)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON inválido'}, status=400)

    return JsonResponse({'error': 'Método não permitido'}, status=405)


@csrf_exempt
def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return JsonResponse({'message': 'Logout realizado com sucesso!'}, status=200)
    return JsonResponse({'error': 'Método não permitido'}, status=405)


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